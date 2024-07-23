from markdown_html import markdown_to_html_node


def main():
    md = """
    This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items
    """

    output = markdown_to_html_node(md)

    print(output.to_html())


main()
