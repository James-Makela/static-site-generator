import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        second_child_node = LeafNode("span", "second child")
        parent_node = ParentNode("div", [child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><span>second child</span></div>",
        )

    def test_to_html_with_tagless_child(self):
        child_node = LeafNode(tag=None, value="some plain text with no tag")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>some plain text with no tag</div>")

    def test_to_html_with_mixed_child_nodes(self):
        child_node = LeafNode("span", "child")
        grandchild_node = LeafNode("p", "some basic p text")
        second_child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><span><p>some basic p text</p></span></div>",
        )

    def test_to_html_with_deep_nesting(self):
        leaf_node = LeafNode("b", "grandchild")
        great_grandchild_node = ParentNode("span", [leaf_node])
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><span><span><b>grandchild</b></span></span></span></div>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_parent_with_missing_tag(self):
        child_node = LeafNode("p", "child node text")
        node = ParentNode(tag=None, children=[child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_with_empty_children_list(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

        another_parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            another_parent_node.to_html()

    def test_to_html_for_parent_with_children_having_empty_strings(self):
        child = LeafNode("b", "")
        parent_node = ParentNode("div", [child])
        self.assertEqual(parent_node.to_html(), "<div><b></b></div>")


if __name__ == "__main__":
    unittest.main
