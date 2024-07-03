import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        self.assertEqual(
            "TextNode(This is a text node, bold, None)", repr(node)
        )

        node3 = TextNode("This is the same.", "bold")
        node4 = TextNode("This is not the same!", "bold")
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", "italic")
        node6 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node5, node6)

        node7 = TextNode("This is a text node", "bold")
        node8 = TextNode("This is a text node", "bold", "not none")
        self.assertNotEqual(node7, node8)
    
    def test_text_to_leaf(self):
        text_node = TextNode("This is bold", "bold")
        leaf_node = LeafNode("b", "This is bold")
        self.assertEqual(print(leaf_node), print(text_node_to_html_node(text_node)))


if __name__ == "__main__":
    unittest.main()