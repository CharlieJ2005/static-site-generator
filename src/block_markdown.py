import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    splits = markdown.split("\n\n")
    for split in splits:
        split = split.strip()
        if split:
            blocks.append(split)
    return blocks


def block_to_blocktype(block):
    lines = block.split("\n")
    if len(lines) == 1 and lines[0].startswith("#"):
        if re.match(r"^#{1,6} ", lines[0]):
            return BlockType.HEADING
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    is_ordered = True
    for idx, line in enumerate(lines):
        expected_prefix = f"{idx+1}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered and len(lines) > 0:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
