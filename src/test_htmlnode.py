import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
        self.assertEqual(
            "HTMLNode(None, None, children: None, {'href': 'https://www.google.com', 'target': '_blank'})", repr(node2)
        )
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node2.props_to_html()
        )


if __name__ == "__main__":
    unittest.main()