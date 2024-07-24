import os
import shutil

from copystatic import copy_static
from generate_pages import extract_title, generate_page, generate_pages_recursive

output_dir = "public"
input_dir = "static"


def main():
    if os.path.exists("public"):
        print("[clearing dir]", output_dir)
        shutil.rmtree(output_dir)

    copy_static(input_dir, output_dir)

    generate_pages_recursive("content", "template.html", "public")


main()
