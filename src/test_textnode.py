import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        print("__eq__: tested")

    def test_url(self):
        node = TextNode("some text", "bold")
        self.assertEqual(node.url, None)
        print("url is None: tested")

    def test_text_is_diff(self):
        node = TextNode("some text", "bold")
        node2 = TextNode("some text", "span")
        self.assertNotEqual(node, node2)
        print("text not __eq__: tested")

if __name__ == "__main__":
    unittest.main()