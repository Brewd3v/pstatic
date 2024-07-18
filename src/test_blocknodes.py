import unittest

from blocknodes import markdown_to_blocks


class TestBlockNodes(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'],
            blocks
        )


if __name__ == "__main__":
    unittest.main()
