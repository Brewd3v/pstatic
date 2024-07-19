import unittest

from blocknodes import (
    block_to_block_type,
    markdown_to_blocks,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list

)


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

    def test_markdown_to_blocks_newlines(self):
        md = """
            This is **bolded** paragraph




            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_heading_1(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("# heading")
        )

    def test_heading_2(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("## heading")
        )

    def test_heading_3(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("# heading")
        )

    def test_heading_4(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("#### heading")
        )

    def test_heading_5(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("##### heading")
        )

    def test_heading_6(self):
        self.assertEqual(
            block_type_heading,
            block_to_block_type("###### heading")
        )

    def test_heading_p(self):
        self.assertEqual(
            block_type_paragraph,
            block_to_block_type("####### heading")
        )

    def test_code(self):
        self.assertEqual(
            block_type_code,
            block_to_block_type("```\nsome code goes here\n```")
        )

    def test_quote(self):
        self.assertEqual(
            block_type_quote,
            block_to_block_type(
                "> some quote\n> like this\n> let's make it three lines")
        )

    def test_unordered_list_star(self):
        self.assertEqual(
            block_type_unordered_list,
            block_to_block_type(
                "* some list\n* like this\n* let's make it three lines")
        )

    def test_unordered_list_dash(self):
        self.assertEqual(
            block_type_unordered_list,
            block_to_block_type(
                "- some list\n- like this\n- let's make it three lines")
        )

    def test_unordered_list_mixed(self):
        self.assertEqual(
            block_type_unordered_list,
            block_to_block_type(
                "- some list\n* like this\n- let's make it three lines")
        )

    def test_ordered_list_in_order(self):
        self.assertEqual(
            block_type_ordered_list,
            block_to_block_type(
                "1. some list\n2. like this\n3. let's make it three lines")
        )

    def test_ordered_list_in_order(self):
        self.assertEqual(
            block_type_ordered_list,
            block_to_block_type(
                "1. some list\n2. like this\n3. let's make it three lines")
        )

    def test_ordered_list_out_order(self):
        self.assertEqual(
            block_type_paragraph,
            block_to_block_type(
                "1. some list\n3. like this\n4. let's make it three lines")
        )

    def test_plain_p(self):
        self.assertEqual(
            block_type_paragraph,
            block_to_block_type("Some plain text")
        )


if __name__ == "__main__":
    unittest.main()
