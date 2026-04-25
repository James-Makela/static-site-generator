import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_is_correct_type(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_not_impleted_error_for_base_class(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_create_node_with_information(self):
        test_props = {
                "href": "https://www.google.com",
                "target": "blank",
            }
        populated_node = HTMLNode(
            tag="a",
            props=test_props
        )
        expected_repr = "HTMLNode(Tag: a, Value: None, Children: None, Props: {'href': 'https://www.google.com', 'target': 'blank'})"
        self.assertEqual(populated_node.tag, "a")
        self.assertEqual(populated_node.props, test_props)
        self.assertEqual(repr(populated_node), expected_repr)

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

    def test_props_to_html_returns_empty_string_with_no_props(self):
        node = HTMLNode("p", "Test paragraph with no props")
        self.assertEqual(node.props_to_html(), "")


class TestLeafNode(unittest.TestCase):
    def test_create_leaf_node_with_information(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Google")
        self.assertEqual(node.props, {"href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode(Tag: a, Value: Google, Props: {'href': 'https://www.google.com'})")

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

    def test_leaf_with_no_tag(self):
        node = LeafNode(None, "This is some raw text")
        self.assertEqual(node.to_html(), "This is some raw text")

    def test_leaf_to_html_with_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
