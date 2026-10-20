import unittest

from tools.governance import run_tests
from tools.governance.tests.helpers import TempRepo


class WorkingTreeHashTests(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()
        self.repo.git_init()
        self.repo.git("config", "core.filemode", "false")
        self.repo.write_text("a.txt", "a\n")
        self.repo.git("add", "-A")
        self.repo.git("commit", "-q", "-m", "base")

    def tearDown(self):
        self.repo.cleanup()

    def test_hash_keeps_a_staged_executable_bit(self):
        self.repo.write_text("hook.sh", "#!/bin/sh\n")
        self.repo.git("add", "hook.sh")
        self.repo.git("update-index", "--chmod=+x", "hook.sh")
        expected = self.repo.git("write-tree").stdout.strip()
        self.assertEqual(run_tests.working_tree_hash(self.repo.root), expected)

    def test_hash_includes_unstaged_changes(self):
        self.repo.write_text("a.txt", "changed\n")
        self.repo.write_text("b.txt", "new\n")
        before = self.repo.git("write-tree").stdout.strip()
        self.assertNotEqual(run_tests.working_tree_hash(self.repo.root), before)
        self.repo.git("add", "-A")
        self.assertEqual(run_tests.working_tree_hash(self.repo.root), self.repo.git("write-tree").stdout.strip())


if __name__ == "__main__":
    unittest.main()
