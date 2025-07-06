import unittest
from block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                (
                    "This is another paragraph with _italic_ text and `code` "
                    "here\n"
                    "This is the same paragraph on a new line"
                ),
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_paragraphs(self):
        md = """
This is the first paragraph.

This is the second paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph.",
                "This is the second paragraph.",
            ],
        )

    def test_markdown_to_blocks_lists(self):
        md = """
- Item one
- Item two

- Item three
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- Item one\n- Item two",
                "- Item three",
            ],
        )

    def test_markdown_to_blocks_mixed(self):
        md = """
Paragraph one.

- List item 1
- List item 2

Paragraph two.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Paragraph one.",
                "- List item 1\n- List item 2",
                "Paragraph two.",
            ],
        )

    def test_markdown_to_blocks_single_block(self):
        md = """Just a single block with no blank lines."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Just a single block with no blank lines.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
