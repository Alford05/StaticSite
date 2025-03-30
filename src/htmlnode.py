class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    
    def __to_html__(self):
        raise NotImplementedError
    
    def __props_to_html__(self);
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




    