from htmlnode import LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node
from splitnodes import split_nodes_delimiter


def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    print(new_nodes)
main()
