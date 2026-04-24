import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_is_correct_type(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_not_impleted_error_for_base_class(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_create_node_with_information(self):
        test_props = {
                "href": "https://www.google.com",
                "target": "blank",
            }
        populated_node = HTMLNode(
            tag="a",
            props=test_props
        )
        self.assertEqual(populated_node.tag, "a")
        self.assertEqual(populated_node.props, test_props)

    def test_props_to_html_returns_correctly(self):
        test_props = {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        props_string = ' href="https://www.google.com" target="_blank"'
        populated_node = HTMLNode(
            tag="a",
            props=test_props
        )
        self.assertEqual(populated_node.props_to_html(), props_string)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a",
            "Google",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is some bold text")
        self.assertEqual(node.to_html(), '<b>This is some bold text</b>')
