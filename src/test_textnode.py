import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode(
            "The cake is a lie",
            TextType.ITALIC,
            "https://www.thinkwithportals.com/"
            )
        node2 = TextNode(
            "The cake is a lie",
            TextType.ITALIC,
            "https://www.thinkwithportals.com/"
            )
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode(
            "And this is another",
            TextType.CODE,
            "https://www.chepek.com"
            )
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("I always tell the truth", TextType.IMAGE)
        node2 = TextNode("I always lie", TextType.LINK, "https://www.com.com")
        self.assertNotEqual(node, node2)

    def test_nourl1(self):
        node = TextNode("Believe in yourself", TextType.TEXT, None)
        node2 = TextNode("Believe in yourself", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_nourl2(self):
        node = TextNode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", TextType.ITALIC)
        node2 = TextNode("ABCDEFGHIJKLMNOPQRSTUVWXYZ", TextType.ITALIC, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
