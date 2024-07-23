import re

from htmlnode import HTMLNode
from textnode import TextNode, text_type_text

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    split = markdown.split("\n\n")
    strip_spaces = map(lambda item: item.strip().replace("  ", ""), split)
    filter_empty = filter(lambda item: item != '', strip_spaces)
    return list(filter_empty)


def block_to_block_type(block):
    if not block:
        raise ValueError("No markdown found")

    if len(re.findall("^#{1,6} ", block)) > 0:
        return block_type_heading
    elif len(re.findall("```(\s*[^`]*?)```", block)) > 0:
        return block_type_code
    elif len(re.findall("^>", block, re.MULTILINE)) > 0:
        return block_type_quote
    elif len(re.findall("^(\* |- )", block, re.MULTILINE)) > 0:
        return block_type_unordered_list
    elif len(re.findall("(\d+)\.", block, re.MULTILINE)) > 0:
        split = re.findall("(\d+)\.", block, re.MULTILINE)
        # check list is in order
        for i in range(len(split)):
            if (i + 1) != int(split[i]):
                return block_type_paragraph

        return block_type_ordered_list
    else:
        return block_type_paragraph
