from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Splits a text node into corresponding parts based on a given delimiter.
    old_nodes -- a list of nodes to convert to html nodes
    delimiter -- the delimiter you are wanting to split on
    text_type -- the type of text to be split out - this will match the delimiter
    """
    new_nodes = []
    for node in old_nodes:
        # We will only be handling text nodes at this stage
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        pieces = node.text.split(delimiter)
        
        # An even number of pieces would indicate an invalid number of delimiters
        if len(pieces) % 2 == 0:
            raise Exception(f"There is not a valid amount of the delimiter in the given string: {node.text}")

        for i, piece in enumerate(pieces):
            # Ignore empty strings
            if not piece:
                continue
            # Odd nodes get turned into text_type nodes
            if i % 2 == 1:
                new_nodes.append(TextNode(piece, text_type))
            # Even nodes are of plain TEXT type
            else:
                new_nodes.append(TextNode(piece, TextType.TEXT))

    return new_nodes
