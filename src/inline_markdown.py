import re
from textnode import TextType, TextNode
from leafnode import LeafNode


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


def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            result_nodes.append(node)
            continue

        curr_pos = 0
        for alt, url in images:
            # Find the image markdown in the text
            img_md = f"![{alt}]({url})"
            idx = text.find(img_md, curr_pos)
            if idx == -1:
                raise ValueError("Invalid markdown: image section not closed")
            # Add text before the image, if any
            if idx > curr_pos:
                before = text[curr_pos:idx]
                if before:
                    result_nodes.append(TextNode(before, TextType.TEXT))
            # Add the image node
            result_nodes.append(TextNode(alt, TextType.IMAGE, url))
            curr_pos = idx + len(img_md)
        # Add any remaining text after the last image
        if curr_pos < len(text):
            result_nodes.append(TextNode(text[curr_pos:], TextType.TEXT))
    return result_nodes


def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            result_nodes.append(node)
            continue

        curr_pos = 0
        for label, url in links:
            link_md = f"[{label}]({url})"
            idx = text.find(link_md, curr_pos)
            if idx == -1:
                raise ValueError("Invalid markdown: link section not closed")
            # Add text before the link, if any
            if idx > curr_pos:
                before = text[curr_pos:idx]
                if before:
                    result_nodes.append(TextNode(before, TextType.TEXT))
            # Add the link node
            result_nodes.append(TextNode(label, TextType.LINK, url))
            curr_pos = idx + len(link_md)
        # Add any remaining text after the last link
        if curr_pos < len(text):
            result_nodes.append(TextNode(text[curr_pos:], TextType.TEXT))
    return result_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    filtered_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT and node.text == "":
            continue
        filtered_nodes.append(node)
    nodes = filtered_nodes
    return nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
