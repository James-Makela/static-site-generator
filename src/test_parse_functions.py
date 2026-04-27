import unittest

from textnode import TextNode, TextType
from parse_functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    # Delimiter type rotated across tests for coverage
    def test_single_delimiter_pair(self):
        node_to_parse = TextNode("part one text `code delimited` part two text", TextType.TEXT)
        parsed_nodes = split_nodes_delimiter([node_to_parse], "`", TextType.CODE)
        expected = [
            TextNode("part one text ", TextType.TEXT),
            TextNode("code delimited", TextType.CODE),
            TextNode(" part two text", TextType.TEXT),
        ]
        self.assertEqual(parsed_nodes, expected)

    def test_delimiter_at_start(self):
        node_to_parse = TextNode("**bold** rest of the text", TextType.TEXT)
        parsed_nodes = split_nodes_delimiter([node_to_parse], "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" rest of the text", TextType.TEXT),
        ]
        self.assertEqual(parsed_nodes, expected)

    def test_delimiter_at_end(self):
        node_to_parse = TextNode("some initial text _italic text_", TextType.TEXT)
        parsed_nodes = split_nodes_delimiter([node_to_parse], "_", TextType.ITALIC)
        expected = [
            TextNode("some initial text ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
        ]
        self.assertEqual(parsed_nodes, expected)

    def test_multiple_delimiters(self):
        node_to_parse = TextNode(
            "Here is some `code` and some more `code text` delimited",
            TextType.TEXT
        )
        parsed_nodes = split_nodes_delimiter([node_to_parse], "`", TextType.CODE)
        expected = [
            TextNode("Here is some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and some more ", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode(" delimited", TextType.TEXT),
        ]
        self.assertEqual(parsed_nodes, expected)

    def test_plain_text_node(self):
        node_to_parse = TextNode("Some plain text", TextType.TEXT)
        parsed_node = split_nodes_delimiter([node_to_parse], "**", TextType.BOLD)
        print(parsed_node)
        self.assertEqual(parsed_node, [node_to_parse])

    def test_mutiple_nodes(self):
        nodes_to_parse = [
            TextNode("text **node** one", TextType.TEXT),
            TextNode("another **text** node with bold", TextType.TEXT),
        ]
        parsed_nodes = split_nodes_delimiter(nodes_to_parse, "**", TextType.BOLD)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("node", TextType.BOLD),
            TextNode(" one", TextType.TEXT),
            TextNode("another ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" node with bold", TextType.TEXT),
        ]
        self.assertEqual(parsed_nodes, expected)

    def test_chained_nodes(self):
        node_to_parse = TextNode(
            "some initial **bold** text and some _italic text_",
            TextType.TEXT
        )
        initial_parse = split_nodes_delimiter([node_to_parse], "**", TextType.BOLD)
        second_parse = split_nodes_delimiter(initial_parse, "_", TextType.ITALIC)
        expected = [
            TextNode("some initial ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text and some ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
        ]
        self.assertEqual(second_parse, expected)

    def test_raises_on_unmatched_delimiter(self):
        node_to_parse = TextNode("some initial text _italic text", TextType.TEXT)
        with self.assertRaises(Exception):
            parsed_nodes = split_nodes_delimiter([node_to_parse], "_", TextType.ITALIC)
