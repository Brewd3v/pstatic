from htmlnode import LeafNode, ParentNode


def main():
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

    node2 = ParentNode(
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

    print(node2.to_html())


main()
