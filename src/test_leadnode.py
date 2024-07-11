import unittest
from leafnode import LeafNode


class TestLeadNode(unittest.TestCase):
    def test_to_html_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_tag(self):
        node = LeafNode(None, value="Some text")
        self.assertEqual(node.to_html(), "Some text")

    def test_to_html_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            "<a href='https://www.google.com'>Click me!</a>"
        )


if __name__ == "__main__":
    unittest.main()
