from splitnodes import extract_markdown_images, split_nodes_link, split_nodes_image, text_to_textnodes
from textnode import TextNode, text_type_text


def main():
    md = TextNode(
        "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", text_type_text)
    print(text_to_textnodes([md]))


main()
