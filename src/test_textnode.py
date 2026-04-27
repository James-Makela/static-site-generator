import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a urlless text node", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.TEXT, None)")


class TestNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node") 

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node") 

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node") 

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node") 

    def test_link(self):
        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("This is an Image", TextType.IMAGE, "https://placehold.net/400x400.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "") 
        self.assertEqual(html_node.props, {"src": "https://placehold.net/400x400.png", "alt": "This is an Image"}) 

    def test_invalid_text_type(self):
        node = TextNode("This is a text node", "invalidtype")
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)

    def test_node_type_is_correct(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)


if __name__ == "__main__":
    unittest.main
