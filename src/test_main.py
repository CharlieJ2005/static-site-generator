import unittest
from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_extra_spaces(self):
        self.assertEqual(
            extract_title("   #    Hello World   "),
            "Hello World"
            )

    def test_h1_not_first_line(self):
        md = "Some intro\n# Title Here\nMore text"
        self.assertEqual(extract_title(md), "Title Here")

    def test_h1_with_trailing_whitespace(self):
        self.assertEqual(extract_title("#   Hello   "), "Hello")

    def test_no_h1_raises(self):
        with self.assertRaises(Exception):
            extract_title("No header here\n## Subheader")

    def test_multiple_h1_returns_first(self):
        md = "# First Title\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")


if __name__ == "__main__":
    unittest.main()
