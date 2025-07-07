import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node
    )


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
            block_to_block_type("# Heading 1"),
            BlockType.HEADING,
        )
        self.assertEqual(
            block_to_block_type("###### Heading 6"),
            BlockType.HEADING,
        )
        self.assertNotEqual(
            block_to_block_type("####### Not a heading"),
            BlockType.HEADING,
        )

    def test_code_block(self):
        code = "```\nprint('hello')\n```"
        self.assertEqual(
            block_to_block_type(code),
            BlockType.CODE,
        )

    def test_quote_block(self):
        quote = "> This is a quote\n> with two lines"
        self.assertEqual(
            block_to_block_type(quote),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        ul = "- item one\n- item two"
        self.assertEqual(
            block_to_block_type(ul),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(
            block_to_block_type(ol),
            BlockType.ORDERED_LIST,
        )
        not_ol = "1. first\n3. not incremented"
        self.assertNotEqual(
            block_to_block_type(not_ol),
            BlockType.ORDERED_LIST,
        )

    def test_paragraph(self):
        para = "Just a normal paragraph of text."
        self.assertEqual(
            block_to_block_type(para),
            BlockType.PARAGRAPH,
        )


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = (
            "\nThis is **bolded** paragraph\ntext in a p\ntag here\n\n"
            "This is another paragraph with _italic_ text and `code` here\n\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and "
            "<code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = (
            "\n```\nThis is text that _should_ remain\n"
            "the **same** even with inline stuff\n```\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "# Heading 1"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1></div>",
        )

    def test_unordered_list(self):
        md = (
            "\n- item one\n- item two\n- item three\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item one</li><li>item two</li>"
            "<li>item three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = (
            "1. first item\n"
            "2. second item\n"
            "3. third item"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first item</li><li>second item</li>"
            "<li>third item</li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = (
            "# Heading\n\n"
            "Paragraph text.\n\n"
            "- item 1\n- item 2\n\n"
            "1. first\n2. second"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>Paragraph text.</p>"
            "<ul><li>item 1</li><li>item 2</li></ul>"
            "<ol><li>first</li><li>second</li></ol></div>",
        )

    def test_quote_block(self):
        md = (
            "> this is a quote\n"
            "> with two lines"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>this is a quote\n"
            "with two lines</blockquote></div>",
        )

    def test_empty_markdown(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_single_line_paragraph(self):
        md = "Just a single line."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>Just a single line.</p></div>")


if __name__ == "__main__":
    unittest.main()
