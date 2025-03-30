class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __to_html__(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for prop, value in self.props.items():
            props_str += f' {prop}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"""HTMLNode(
        tag: {self.tag}, 
        value: {self.value}, 
        children: {self.children}, 
        props: {self.props}
        )"""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, [], props)
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        html = f"<{self.tag}"
        if self.props:
            for prop_name, prop_value in self.props.items():
                html += f' {prop_name}="{prop_value}"'
        html += f">{self.value}</{self.tag}>"
        return html


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, [], children, props)
        if not isinstance(children, list) or children == []:
            raise ValueError("ParentNode must have a non-empty list of children")

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have a child")
        html = f"<{self.tag}>"
        for child in self.children:
            html += f"{child.to_html()}"
        html += f"</{self.tag}>"
        return html






    
