import re
import unittest

from tools.governance import common


class NormativeHashTests(unittest.TestCase):
    def base(self):
        return {
            "id": "REQ-GL-001",
            "type": "requirement",
            "title": "Post approved journals",
            "status": "Proposed",
            "version": 1,
            "tier": 2,
            "normative": {"statement": "When X, the system shall Y.", "rules": ["r1"]},
            "links": {"derives_from": ["S1-2.2.4-c01", "BO-01"], "related": ["DEC-0001"]},
        }

    def test_format(self):
        self.assertRegex(common.normative_hash(self.base()), r"^sha256:[0-9a-f]{64}$")

    def test_whitespace_and_key_order_do_not_change_hash(self):
        a = self.base()
        b = self.base()
        b["normative"] = {"rules": ["r1"], "statement": "  When  X,\r\n the system   shall Y.  "}
        self.assertEqual(common.normative_hash(a), common.normative_hash(b))

    def test_normative_change_changes_hash(self):
        a = self.base()
        b = self.base()
        b["normative"]["statement"] = "When X, the system shall Z."
        self.assertNotEqual(common.normative_hash(a), common.normative_hash(b))

    def test_editorial_fields_are_not_normative(self):
        a = self.base()
        b = self.base()
        b.update(title="Another title", status="Approved", version=7, owner="someone")
        self.assertEqual(common.normative_hash(a), common.normative_hash(b))

    def test_normative_links_are_sorted_and_other_links_ignored(self):
        a = self.base()
        b = self.base()
        b["links"] = {"derives_from": ["BO-01", "S1-2.2.4-c01"], "related": ["DEC-0002"]}
        self.assertEqual(common.normative_hash(a), common.normative_hash(b))
        c = self.base()
        c["links"]["governed_by"] = ["POL-001"]
        self.assertNotEqual(common.normative_hash(a), common.normative_hash(c))

    def test_tier_is_normative(self):
        a = self.base()
        b = self.base()
        b["tier"] = 1
        self.assertNotEqual(common.normative_hash(a), common.normative_hash(b))


class FrontMatterTests(unittest.TestCase):
    def test_parse(self):
        meta, body = common.parse_front_matter("---\nid: X-1\ntitle: T\n---\n\nBody text\n")
        self.assertEqual(meta, {"id": "X-1", "title": "T"})
        self.assertEqual(body.strip(), "Body text")

    def test_crlf(self):
        meta, _ = common.parse_front_matter("---\r\nid: X-1\r\n---\r\nBody\r\n")
        self.assertEqual(meta, {"id": "X-1"})

    def test_no_front_matter(self):
        meta, body = common.parse_front_matter("# Title\n\ntext\n")
        self.assertIsNone(meta)
        self.assertIn("Title", body)


class UlidTests(unittest.TestCase):
    def test_format(self):
        self.assertRegex(common.new_ulid(), r"^[0-9A-HJKMNP-TV-Z]{26}$")

    def test_time_ordered(self):
        early = common.new_ulid(timestamp_ms=1_000_000)
        late = common.new_ulid(timestamp_ms=2_000_000)
        self.assertLess(early, late)


class IdKindTests(unittest.TestCase):
    def test_known_ids(self):
        ulid = common.new_ulid()
        cases = {
            "REQ-GL-001": "REQ",
            "US-GL-001": "US",
            "AC-US-GL-001-01": "AC",
            "DEC-0001": "DEC",
            "GOV-METHOD": "GOV",
            "SRC-001": "SRC",
            "S1-2.2.4-c07": "S1",
            f"AREQ-{ulid}": "AREQ",
            f"APR-{ulid}": "APR",
            "GATE-0": "GATE",
            "GATE-A-R1": "GATE",
            "RISK-001": "RISK",
        }
        for identifier, kind in cases.items():
            with self.subTest(identifier=identifier):
                self.assertEqual(common.id_kind(identifier), kind)

    def test_invalid_ids(self):
        for identifier in ("REQ-1", "DEC-1", "AREQ-123", "hello", "US-gl-001"):
            with self.subTest(identifier=identifier):
                self.assertIsNone(common.id_kind(identifier))


if __name__ == "__main__":
    unittest.main()
