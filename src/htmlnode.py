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
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props})"

    def __str__(self):
        string = ""
        string += f"Tag: {self.tag}\n"
        string +=f"Value: {self.value}\n"
        string += f"Children: \n"
        if not self.children or len(self.children) == 0:
            string +="No children\n"
        else:
            for child in self.children:
                string += f"\t{child}\n"
        string += f"Props: \n"
        if not self.props or len(self.props) == 0:
            string += "No props\n"
        else:
            for prop in self.props:
                string += f"\t{prop}: {self.props[prop]}\n"

        return string
        

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
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Props: {self.props})"

    def __str__(self):
        string = ""
        string += f"Tag: {self.tag}\n"
        string +=f"Value: {self.value}\n"
        string += f"Props: \n"
        if not self.props or len(self.props) == 0:
            string += "No props\n"
        else:
            for prop in self.props:
                string += f"\t{prop}: {self.props[prop]}\n"

        return string


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent node must have one or more children")

        html_string = ""
        if self.props:
            html_string += f"<{self.tag}{self.props_to_html()}>"
        else:
            html_string += f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()

        html_string += f"</{self.tag}>"
        return html_string
        
