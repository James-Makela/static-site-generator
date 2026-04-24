import unittest

from htmlnode import HTMLNode

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
