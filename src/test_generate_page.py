import unittest

from generate_page import extract_title


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("""
        # heading

        some text""")
        self.assertEqual(title, "heading")

