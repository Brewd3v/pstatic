

import re
from blocknodes import block_to_block_type, markdown_to_blocks


def main():
    md = """
    - some list
    * like this
    - let's make it three lines
    """

    blocks = markdown_to_blocks(md)
    block_type = block_to_block_type(blocks[0])

    print(blocks)
    print(block_type)


main()
