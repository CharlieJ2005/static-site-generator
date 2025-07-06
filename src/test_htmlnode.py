import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode("a", "Link", None, {"href": "https://example.com"})
        node.props = {"href": "https://example.com"}
        self.assertEqual(node.props_to_html(), 'href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("img", None, None, {"src": "img.png", "alt": "desc"})
        node.props = {"src": "img.png", "alt": "desc"}
        self.assertEqual(node.props_to_html(), 'src="img.png" alt="desc"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div", None, None, {})
        node.props = {}
        self.assertEqual(node.props_to_html(), '')


if __name__ == "__main__":
    unittest.main()
