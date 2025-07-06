from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: missing tag")
        if self.children is None:
            raise ValueError("Error: missing children")
        props_html = self.props_to_html()
        if props_html:
            props_html = " " + props_html
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
