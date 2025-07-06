class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = None
        self.value = None
        self.children = None
        self.props = None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""
        for key, value in self.props.items():
            html_string += f'{key}="{value}" '
        html_string = html_string[:-1]
        return html_string

    def __repr__(self):
        return (
            f"HTMLNode({self.tag}, {self.value}, "
            f"{self.children}, {self.props})"
        )
