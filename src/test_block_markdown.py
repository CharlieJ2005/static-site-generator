import unittest
from block_markdown import markdown_to_blocks, block_to_blocktype, BlockType


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


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(
            block_to_blocktype("# Heading 1"),
            BlockType.HEADING,
        )
        self.assertEqual(
            block_to_blocktype("###### Heading 6"),
            BlockType.HEADING,
        )
        self.assertNotEqual(
            block_to_blocktype("####### Not a heading"),
            BlockType.HEADING,
        )

    def test_code_block(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(
            block_to_blocktype(code),
            BlockType.CODE,
        )

    def test_quote_block(self):
        quote = "> This is a quote\n> with two lines"
        self.assertEqual(
            block_to_blocktype(quote),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        ul = "- item one\n- item two"
        self.assertEqual(
            block_to_blocktype(ul),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(
            block_to_blocktype(ol),
            BlockType.ORDERED_LIST,
        )
        not_ol = "1. first\n3. not incremented"
        self.assertNotEqual(
            block_to_blocktype(not_ol),
            BlockType.ORDERED_LIST,
        )

    def test_paragraph(self):
        para = "Just a normal paragraph of text."
        self.assertEqual(
            block_to_blocktype(para),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()
