from splitnodes import extract_markdown_images, split_nodes_link, split_nodes_image
from textnode import TextNode, text_type_text


def main():
    node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )

    # print(split_nodes_link([node]))
    print(split_nodes_image([node]))


main()
