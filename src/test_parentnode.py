import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
            )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("span", "one")
        child2 = LeafNode("span", "two")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>one</span><span>two</span></div>"
            )

    def test_to_html_with_multiple_nested_parents(self):
        leaf = LeafNode("em", "deep")
        inner_parent = ParentNode("span", [leaf])
        middle_parent = ParentNode("section", [inner_parent])
        outer_parent = ParentNode("div", [middle_parent])
        self.assertEqual(
            outer_parent.to_html(),
            "<div><section><span><em>deep</em></span></section></div>"
        )

    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode(
            "div",
            [child],
            {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )

    def test_to_html_with_no_tag_raises(self):
        child = LeafNode("span", "child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_no_children_raises(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_empty_children_list(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_to_html_with_mixed_leaf_and_parent_children(self):
        leaf1 = LeafNode("b", "bold")
        leaf2 = LeafNode("i", "italic")
        child_parent = ParentNode("span", [leaf2])
        parent = ParentNode("div", [leaf1, child_parent])
        self.assertEqual(
            parent.to_html(),
            "<div><b>bold</b><span><i>italic</i></span></div>"
        )


if __name__ == "__main__":
    unittest.main()
