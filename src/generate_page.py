import os
from blocknodes import markdown_to_blocks
from markdown_html import markdown_to_html_node


def extract_title(markdown):
    title = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            title = block[2:]

    if len(title) > 0:
        return title
    else:
        raise Exception("No title found.")


def generate_page(from_path, template_path, dest_path):
    print("[Generating page] from", from_path, "->", dest_path)
    try:
        with open(from_path) as md_file:
            md = md_file.read()

            try:
                template = open(template_path)
            except FileNotFoundError:
                print("[error] template", template_path, " was not found")

            template_content = template.read()

            html = markdown_to_html_node(md).to_html()
            page_title = extract_title(md)

            template_content = template_content.replace("{{ Title }}", page_title)
            template_content = template_content.replace("{{ Content }}", html)

            file_path = os.path.dirname(dest_path)

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            with open(dest_path, "w") as html_file:
                html_file.write(template_content)

    except FileNotFoundError:
        print("[error]", from_path, "was not found")
