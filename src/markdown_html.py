import re

from blocknodes import (
    block_to_block_type,
    markdown_to_blocks
)
from htmlnode import ParentNode
from splitnodes import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    new_blocks = []

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        html_node = block_to_html_node(block)
        new_blocks.append(html_node)

    return ParentNode('div', new_blocks, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    match block_type:
        case "paragraph":
            return paragraph_to_html_node(block)

        case "heading":
            return heading_to_html_node(block)

        case "code":
            return code_to_html_node(block)

        case "quote":
            return blockquote_to_node(block)

        case "unordered_list":
            return ul_to_html_node(block)

        case "ordered_list":
            return ol_to_html_node(block)

    raise ValueError("Invalid block type")

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def heading_to_html_node(block):
    heading_text = heading_md_to_text(block)
    children = text_to_children(heading_text)
    tag = heading_tag_type(block)
    if len(children) > 0:
        return ParentNode(
            tag,
            children=children
        )
    return ParentNode(tag, heading_text)


def heading_tag_type(heading_block):
    if len(re.findall("^#{1} ", heading_block)):
        return "h1"
    elif len(re.findall("^#{2} ", heading_block)):
        return "h2"
    elif len(re.findall("^#{3} ", heading_block)):
        return "h3"
    elif len(re.findall("^#{4} ", heading_block)):
        return "h4"
    elif len(re.findall("^#{5} ", heading_block)):
        return "h5"
    elif len(re.findall("^#{6} ", heading_block)):
        return "h6"


def heading_md_to_text(block):
    return re.sub("^#{1,6} ", '', block)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def blockquote_to_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def ul_to_html_node(block):
    items = block.split("\n")
    parent_items = []

    for item in items:
        text = item[2:]
        children = text_to_children(text)
        parent_items.append(ParentNode("li", children))

    return ParentNode("ul", parent_items)


def ol_to_html_node(block):
    items = block.split("\n")
    parent_items = []

    for item in items:
        text = item[3:]
        children = text_to_children(text)
        parent_items.append(ParentNode("li", children))

    return ParentNode("ol", parent_items)
