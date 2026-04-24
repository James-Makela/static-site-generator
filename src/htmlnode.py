class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method must be defined in the child class")

    # This will return a formatted string representing the HTML attributes for a node
    def props_to_html(self):
        props_string = ""
        if not self.props or len(self.props) == 0:
            return props_string
        for key in self.props:
            props_string += f" {key}="
            props_string += f'"{self.props[key]}"'
        
        return props_string

    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Children: ")
        if not self.children or len(self.children) == 0:
            print("No children")
        print(f"Props: ")
        if not self.props or len(self.props) == 0:
            print("No props")
        

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All Leaf Nodes must have a value")
        if self.tag is None:
            return self.value
        
        html_string = ""

        if self.props:
            html_string += f"<{self.tag}{self.props_to_html()}>"
        else:
            html_string += f"<{self.tag}>"

        html_string += f"{self.value}</{self.tag}>"

        return html_string

    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Props: ")
        if not self.props or len(self.props) == 0:
            print("No props")

