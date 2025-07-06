from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error: missing value")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        if props_html:
            props_html = " " + props_html
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def props_to_html(self):
        return super().props_to_html()
