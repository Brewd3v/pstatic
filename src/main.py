from htmlnode import LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node


def main():
    node = TextNode("Here is some text", "link", "https://www.google.com")
    node_html = text_node_to_html_node(node)

    print(node_html)
main()
