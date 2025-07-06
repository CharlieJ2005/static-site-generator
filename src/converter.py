import re
from textnode import TextType, TextNode
from leafnode import LeafNode
from parentnode import ParentNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(
                "img",
                "",
                {"src": text_node.url, "alt": text_node.text}
                )
        case _:
            raise Exception("Error: invalid type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        split_parts = node.text.split(delimiter)
        if len(split_parts) % 2 == 0:
            raise Exception("Error: invalid Markdown syntax")
        for i, part in enumerate(split_parts):
            if part == "":
                continue
            if i % 2 == 0:
                final_list.append(TextNode(part, TextType.TEXT))
            else:
                final_list.append(TextNode(part, text_type))
    return final_list


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
