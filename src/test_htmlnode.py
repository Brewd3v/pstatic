import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("a", "Link to website", props={
            "href": "https://www.google.com",
            "target": "_blank"
        })

        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("a", "Link to website", props={
            "href": "https://www.google.com",
            "target": "_blank"
        })

        self.assertEqual(node.props_to_html(),
                         " href='https://www.google.com' target='_blank'")

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            repr(node),
            "HTMLNode(None, None, None, None)"
        )

    # LeafNode
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

    # ParentNode
    def test_tag(self):
        node = ParentNode(None, None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_children(self):
        node = ParentNode("a", [], None)
        self.assertRaises(ValueError, node.to_html)

    def test_html_leafnodes_only(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_html_parent_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
            {
                "aria-label" : "Some helpful intro",
                "title": "This is the title"
            }
        )
        self.assertEqual(node.to_html(), "<p aria-label='Some helpful intro' title='This is the title'><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_html_nested_parentnodes(self):
        node = ParentNode(
            "html",
            [
                ParentNode(
                    "body",
                    [
                        ParentNode(
                            "main",
                            [
                                ParentNode("div", [
                                    LeafNode("h1", "Welcome to my website!"),
                                    LeafNode("a", "Link to google page", {
                                        "href": "https://www.google.com",
                                        "target": "_blank"
                                    })
                                ]),
                                ParentNode(
                                    "p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                        ParentNode(
                                            "p",
                                            [
                                                LeafNode("b", "Nested Bold text"),
                                                LeafNode(
                                                    None, "Nested Normal text"),
                                                LeafNode(
                                                    "i", "Nested italic text"),
                                                LeafNode(
                                                    None, "Nested Normal text"),
                                            ],
                                        )
                                    ],
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<html><body><main><div><h1>Welcome to my website!</h1><a href='https://www.google.com' target='_blank'>Link to google page</a></div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Nested Bold text</b>Nested Normal text<i>Nested italic text</i>Nested Normal text</p></p></main></body></html>")


if __name__ == "__main__":
    unittest.main()
