"""PreToolUse guard for TIQACC.

Blocks, for every actor:
  - writes to protected paths (registered sources, decision records, capture state, git internals)
    and to network paths;
  - rewriting an existing record under ledger/.
Blocks, for agents (agent_type in the hook input; a subagent without one counts as unknown):
  - file writes outside the agent's scope, including anywhere outside the repository;
  - reads (Read, Grep, Glob) outside the repository;
  - shell commands outside the agent's shell profile; any command substitution, variable, brace or
    tilde expansion, background job, here-document or redirection; options that write files or run
    programs, however they are quoted or escaped; and any path outside the repository.
Blocks, for the orchestrator:
  - shell commands that touch a protected path with anything but a known read-only command. Paths
    are resolved, so relative, disguised and 8.3 short spellings count;
  - pushing, force operations, hard resets, recursive deletes, skipping git hooks, and approving or
    merging pull requests.

Tool paths are judged as Claude Code resolves them: trimmed of whitespace and a byte-order mark,
with a leading '~' expanded.

This is a guardrail against mistakes and casual misuse, not a security boundary: a program run
under the same OS account can still write anywhere (RISK-003). Exit code 2 blocks the tool call
and shows the reason to Claude. Any internal error also exits 2 (fail closed). Scopes live in
.claude/hooks/agent-scopes.json.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.governance import common  # noqa: E402

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}
READ_TOOLS = {"Read", "Grep", "Glob"}

BENIGN_REDIRECTS = re.compile(r"\d?>&\d|\d?>\s*/dev/null|\d?>\s*\$null|\d?>\s*nul\b", re.IGNORECASE)
NETWORK_PATH = re.compile(r"^//(?![?.]/[a-zA-Z]:)")
# The shell removes quotes and escapes before a program sees its arguments.
UNQUOTE = re.compile(r"[\"'`\\]")
# A glob pattern, or one of its brace alternatives, that starts at a root, drive or home folder,
# names a drive anywhere, or climbs out with '..'. Applied with backslashes turned into slashes.
GLOB_ESCAPE = re.compile(r"(?:^|[{,])\s*(?:[/~]|[A-Za-z]:)|:|(?:^|[/{,])\.\.(?:$|[/},])")
# Syntax from which a matcher or a shell could build '..', a root or a home folder that the text does
# not show. Applied to the pattern as written. '*.{md,yaml}', '{a,b}.md', '*.[ch]' and '**/.*' pass.
GLOB_SYNTAX_PARTS = (
    r"\.\.",  # two dots anywhere
    r"[{,\[\\]\.",  # a dot after a brace, comma, bracket or escape
    r"\.[},\]]",  # a dot before a closing brace, comma or bracket
    r"\{,|,,|,\}",  # an empty brace alternative
    r"[@+*?!]\(",  # an extglob group
    r"\[[\\/]",  # a bracket that starts with a slash
    r"(?:^|[/\\{,])\.[?*\[{@+!(][^/\\]*[/\\]",  # a folder segment of a dot and a wildcard
    r"[$'\"`]",  # shell variables, quotes and command substitution
)
GLOB_SYNTAX_ESCAPE = re.compile("|".join(GLOB_SYNTAX_PARTS))
# Claude Code trims whitespace and a byte-order mark from a tool's path and expands a leading '~'
# (observed in 2.1.301 for Read, Write, Grep and Glob), so the guard judges the path the tool uses.
PADDING = re.compile(r"^[\s\ufeff]+|[\s\ufeff]+$")

# Agents: shell features none of their commands needs. `$` covers substitution, variables and
# ANSI-C quoting; braces and a leading tilde are expansions too.
AGENT_FORBIDDEN = re.compile(r"`|\$|[{}]|(?:^|[\s=:])~|<\(|>\(|@\(|<<|(?<![&>])&(?![&>])")
AGENT_SPLIT = re.compile(r"\s*(?:&&|\|\||;|\||\r?\n)\s*")

# Orchestrator: statements, pipeline elements, and the commands allowed next to a protected path.
STATEMENT_SPLIT = re.compile(r"\s*(?:&&|\|\||;|\r?\n|(?<![&>|])&(?![&>]))\s*")
PIPE_SPLIT = re.compile(r"(?<!\|)\|(?!\|)")
READ_ONLY = re.compile(
    r"^(?:"
    r"(?:ls|dir|cat|type|head|tail|wc|stat|cmp|diff|grep|egrep|fgrep|sha256sum|sha1sum|md5sum|cksum|b2sum)(?:\s|$)"
    r"|rg(?:\s|$)(?!.*\s--pre(?:=|\s|$))"
    r"|find(?:\s|$)(?!.*\s-(?:exec|execdir|ok|okdir|delete|fprint0?|fprintf|fls)(?:\s|$))"
    r"|git(?:\s+-C\s+\S+|\s+--no-pager)*\s+"
    r"(?:log|show|diff|status|ls-files|ls-tree|blame|rev-parse|cat-file|add|commit)(?:\s|$)(?!.*\s--output(?:=|\s|$))"
    r"|(?:python3?|py)\s+tools/governance/(?:check|trace)\.py(?:\s|$)"
    r"|(?:python3?|py)\s+tools/governance/approvals\.py\s+(?:status|hash)(?:\s|$)"
    r"|(?:Get-Content|gc|Get-ChildItem|gci|Get-Item|gi|Get-FileHash|Select-String|sls|Test-Path|Resolve-Path"
    r"|Format-Hex|Measure-Object)(?:\s|$)"
    r")",
    re.IGNORECASE,
)
# Commands that only transform their input; allowed after a read-only command in a pipeline.
FILTERS = re.compile(
    r"^(?:sort|uniq|cut|tr|nl|column|jq|Sort-Object|Select-Object|select|Group-Object|Format-Table|ft"
    r"|Format-List|fl|Out-String|ConvertFrom-Json|ConvertTo-Json)(?:\s|$)",
    re.IGNORECASE,
)
EXPANSIONS = re.compile(r"`|\$|<\(|>\(|@\(|\{")
REDIRECT_TARGET = re.compile(r"[\d*]?>>?\s*([^\s;|&<>]+)")
CHANGE_DIRECTORY = re.compile(r"^(?:cd|chdir|pushd|Set-Location|sl|Push-Location)\s+(\S+)", re.IGNORECASE)
GIT_DIRECTORY = re.compile(r"(?:^|\s)git\s+(?:\S+\s+)*?-C\s+(\S+)")
TOKEN_SPLIT = re.compile(r"[\s;|&()<>{}=,]+")
QUOTES = re.compile(r"['\"`]")


@dataclass
class Decision:
    allowed: bool
    reason: str = ""


def allow() -> Decision:
    return Decision(True)


def block(reason: str) -> Decision:
    return Decision(False, reason)


# --------------------------------------------------------------------------- protected paths


def _fragments(protected) -> list:
    """Literal leading part of each protected pattern, for spotting protected paths in text."""
    fragments = []
    for pattern in protected:
        literal = re.split(r"[*?\[]", pattern, maxsplit=1)[0].lower()
        if literal:
            fragments.append(literal)
    return fragments


def _is_protected(rel: str, protected) -> bool:
    """True for a protected path, or for a protected folder itself."""
    return common.glob_match(rel, protected) or common.glob_match(rel.rstrip("/") + "/x", protected)


def _normalised(text: str) -> list:
    """Spellings of a command for literal matching: quotes removed, backslashes as separators or dropped."""
    lowered = QUOTES.sub("", text.lower())
    variants = []
    for variant in (lowered.replace("\\", "/"), lowered.replace("\\", "")):
        variant = re.sub(r"/(?:\./)+", "/", variant)
        variants.append(re.sub(r"/{2,}", "/", variant))
    return variants


def _tokens(text: str):
    """Words of a command that may be paths, without quotes or option names."""
    for raw in TOKEN_SPLIT.split(text):
        token = QUOTES.sub("", raw)
        if token.startswith("-"):
            if ":" not in token:
                continue
            token = token.split(":", 1)[1]
        if token and "$" not in token and not token.replace("\\", "/").startswith("//"):
            yield token


def _resolve(token: str, base: Path, root: Path) -> list:
    """Repository-relative paths a token can name from `base`, with globs expanded."""
    candidates = [token]
    if any(character in token for character in "*?["):
        candidates += glob.glob(os.path.join(str(base), token))[:500]
    found = []
    for candidate in candidates:
        try:
            rel = common.repo_relative(candidate, root, base=base)
        except (OSError, ValueError):
            continue
        if rel is not None:
            found.append(rel)
    return found


def _references_protected(text: str, root: Path, directories: list, protected) -> bool:
    fragments = _fragments(protected)
    if any(fragment in variant for fragment in fragments for variant in _normalised(text)):
        return True
    return any(
        _is_protected(rel, protected)
        for token in _tokens(text)
        for base in directories
        for rel in _resolve(token, base, root)
    )


def _outside_repository(text: str, root: Path):
    """The first word of a command that names a path outside the repository, or None."""
    for raw in TOKEN_SPLIT.split(text):
        token = QUOTES.sub("", raw)
        if token.startswith("-"):
            if ":" not in token:
                continue
            token = token.split(":", 1)[1]
        if not token:
            continue
        if token.startswith("//"):
            return token
        try:
            if common.repo_relative(token, root) is None:
                return token
        except (OSError, ValueError):
            return token
    return None


def _read_only(element: str) -> bool:
    """A known read-only command, both as written and as the shell passes it (quotes removed)."""
    return bool(READ_ONLY.match(element.replace("\\", "/")) and READ_ONLY.match(UNQUOTE.sub("", element)))


def _working_directories(statements: list, cwd: Path) -> list:
    """The session's directory plus every directory the command may switch to (cd, git -C)."""
    directories = [cwd]
    for statement in statements:
        for element in PIPE_SPLIT.split(statement):
            element = element.strip()
            targets = GIT_DIRECTORY.findall(element)
            change = CHANGE_DIRECTORY.match(element)
            if change:
                targets.append(change.group(1))
            for target in targets:
                for base in list(directories):
                    try:
                        directory = Path(common.canonical_path(QUOTES.sub("", target), base))
                    except (OSError, ValueError):
                        continue
                    if directory not in directories:
                        directories.append(directory)
    return directories[:16]


# --------------------------------------------------------------------------- decisions


def _tool_path(text) -> str:
    """A tool's path argument as Claude Code resolves it: trimmed, with a leading '~' expanded."""
    text = PADDING.sub("", str(text))
    return os.path.expanduser(text) if text.startswith("~") else text


def _decide_write(path_text, root: Path, agent, scopes) -> Decision:
    path_text = _tool_path(path_text) if path_text else path_text
    if not path_text:
        return block("file write without a path")
    if NETWORK_PATH.match(str(path_text).replace("\\", "/")):
        return block(f"writes to network paths are not allowed ({path_text})")
    try:
        rel = common.repo_relative(path_text, root)
    except (OSError, ValueError) as error:
        return block(f"cannot resolve {path_text}: {error}")
    if rel is None:
        if agent:
            return block(f"agent '{agent}' may write only inside its scope in the repository, not {path_text}")
        return allow()
    if _is_protected(rel, scopes.get("protected")):
        return block(f"{rel} is protected (registered source, decision record or local state); see CLAUDE.md rules 6 and 7")
    if common.glob_match(rel, scopes.get("append_only")) and (root / rel).exists():
        return block(f"{rel} is an existing record; records are never edited, so create a new record instead")
    if agent:
        config = (scopes.get("agents") or {}).get(agent) or scopes.get("unknown_agent") or {"write": []}
        if not common.glob_match(rel, config.get("write")):
            return block(f"agent '{agent}' may not write {rel}; its scope is {config.get('write') or 'nothing'}")
        denied = [pattern for pattern in config.get("deny") or [] if common.glob_match(rel, [pattern])]
        if denied:
            return block(f"agent '{agent}' may not write {rel}; its scope excludes {denied}")
    return allow()


def _decide_read(tool: str, tool_input: dict, root: Path, agent: str) -> Decision:
    """Agents read only inside the repository."""
    patterns = [PADDING.sub("", str(tool_input.get("pattern") or ""))] if tool == "Glob" else []
    if tool == "Grep" and tool_input.get("glob"):
        patterns.append(PADDING.sub("", str(tool_input["glob"])))
    for pattern in patterns:
        if GLOB_ESCAPE.search(pattern.replace("\\", "/")) or GLOB_SYNTAX_ESCAPE.search(pattern):
            return block(
                f"agent '{agent}' may read only inside the repository; pattern {pattern} names a root, "
                "drive or home folder, has '..', or uses glob syntax that could form one of them. "
                "Use a relative pattern and the path argument"
            )
    candidates = [_tool_path(tool_input[key]) for key in ("file_path", "path") if tool_input.get(key)]
    if tool == "Glob":
        literal = re.split(r"[*?\[{]", patterns[0], maxsplit=1)[0]
        if literal:
            base = _tool_path(tool_input["path"]) if tool_input.get("path") else None
            candidates.append(literal if base is None or os.path.isabs(literal) else os.path.join(base, literal))
    for candidate in candidates:
        if NETWORK_PATH.match(candidate.replace("\\", "/")):
            return block(f"agent '{agent}' may not read network paths ({candidate})")
        try:
            rel = common.repo_relative(candidate, root)
        except (OSError, ValueError) as error:
            return block(f"cannot resolve {candidate}: {error}")
        if rel is None:
            return block(f"agent '{agent}' may read only inside the repository, not {candidate}")
    return allow()


def _agent_shell(command: str, agent: str, root: Path, scopes) -> Decision:
    config = (scopes.get("agents") or {}).get(agent) or scopes.get("unknown_agent") or {}
    profile = (scopes.get("shell_profiles") or {}).get(config.get("shell", ""), {})
    text = BENIGN_REDIRECTS.sub(" ", command.replace("\\", "/"))
    if AGENT_FORBIDDEN.search(text):
        return block(
            f"agent '{agent}' may not use command substitution, variables, brace or tilde expansion, "
            "background jobs or here-documents"
        )
    if ">" in text:
        return block(f"agent '{agent}' may not redirect output to files")
    bare = UNQUOTE.sub("", BENIGN_REDIRECTS.sub(" ", command))
    for pattern in scopes.get("agent_shell_deny") or []:
        if re.search(pattern, text) or re.search(pattern, bare):
            return block(f"agent '{agent}' may not use an option that writes files or runs programs ({pattern})")
    allowed = [re.compile(pattern) for pattern in profile.get("allow", [])]
    for part in AGENT_SPLIT.split(text.strip()):
        if part and not any(pattern.search(part) for pattern in allowed):
            return block(f"agent '{agent}' may not run '{part}' (shell profile '{config.get('shell')}')")
    outside = _outside_repository(text, root)
    if outside:
        return block(f"agent '{agent}' may name only paths inside the repository, not {outside}")
    return allow()


def _orchestrator_shell(command: str, root: Path, cwd: Path, scopes) -> Decision:
    text = BENIGN_REDIRECTS.sub(" ", command)
    spellings = (text.replace("\\", "/"), UNQUOTE.sub("", text))
    for pattern in ((scopes.get("shell_profiles") or {}).get("orchestrator") or {}).get("deny", []):
        if any(re.search(pattern, spelling, re.IGNORECASE) for spelling in spellings):
            return block(f"command matches a blocked pattern ({pattern}); a person must do this")
    protected = scopes.get("protected") or []
    statements = [statement for statement in STATEMENT_SPLIT.split(text) if statement and statement.strip()]
    directories = _working_directories(statements, cwd)
    for statement in statements:
        elements = [element.strip() for element in PIPE_SPLIT.split(statement) if element.strip()]
        touching = [_references_protected(element, root, directories, protected) for element in elements]
        if not any(touching):
            continue
        for element, touches in zip(elements, touching):
            if EXPANSIONS.search(element):
                return block(
                    f"'{element}' uses a substitution, variable or script block next to a protected path"
                )
            if touches:
                if not _read_only(element):
                    return block(
                        f"'{element}' touches a protected path, which only read-only commands may do; "
                        "see CLAUDE.md rules 6 and 7"
                    )
                if any(_references_protected(t, root, directories, protected) for t in REDIRECT_TARGET.findall(element)):
                    return block(f"'{element}' redirects output into a protected path")
            elif not (_read_only(element) or FILTERS.match(element.replace("\\", "/"))):
                return block(f"'{element}' receives output naming a protected path; only read-only commands and filters may")
    return allow()


def decide(payload: dict, root: Path) -> Decision:
    root = Path(root)
    scopes_path = root / ".claude/hooks/agent-scopes.json"
    if not scopes_path.is_file():
        raise FileNotFoundError(f"missing {scopes_path}")
    scopes = json.loads(scopes_path.read_text(encoding="utf-8"))
    tool = payload.get("tool_name") or ""
    tool_input = payload.get("tool_input") or {}
    agent = payload.get("agent_type") or ("unknown" if payload.get("agent_id") else None)
    if tool in WRITE_TOOLS:
        path_text = tool_input.get("file_path") or tool_input.get("notebook_path") or tool_input.get("path")
        return _decide_write(path_text, root, agent, scopes)
    if tool in READ_TOOLS:
        return _decide_read(tool, tool_input, root, agent) if agent else allow()
    if tool in SHELL_TOOLS:
        command = str(tool_input.get("command") or "")
        if agent:
            return _agent_shell(command, agent, root, scopes)
        return _orchestrator_shell(command, root, Path(payload.get("cwd") or root), scopes)
    return allow()


def main() -> int:
    try:
        payload = json.loads(sys.stdin.read())
        root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd())
        decision = decide(payload, root)
    except Exception as error:  # fail closed
        print(f"TIQACC governance guard failed closed: {error}", file=sys.stderr)
        return 2
    if decision.allowed:
        return 0
    print(f"Blocked by the TIQACC governance guard: {decision.reason}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
