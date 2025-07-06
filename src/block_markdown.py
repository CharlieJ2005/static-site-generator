from enum import Enum

def markdown_to_blocks(markdown):
    blocks = []
    splits = markdown.split("\n\n")
    for split in splits:
        split = split.strip()
        if split:
            blocks.append(split)
    return blocks
