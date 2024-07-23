import os
import shutil

from copystatic import copy_static

output_dir = "public"
input_dir = "static"


def main():
    if os.path.exists("public"):
        print("[clearing dir]", output_dir)
        shutil.rmtree(output_dir)

    copy_static(input_dir, output_dir)



main()
