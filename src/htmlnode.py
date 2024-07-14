class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        str=""
        for keys in self.props:
            str+=" "+f"{keys}=\"{self.props[keys]}\""
        return str
    def __repr__(self):
        return f"HTMLNode({self.tag} ,{self.value} ,{self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if(self.value==None):
            raise ValueError("All leaf nodes must have a value")
        if(self.tag==None):
            return self.value
        if(self.props==None):
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag} ,{self.value} , {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag=None,children=None,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if(self.tag==None):
            raise ValueError("Parent node needs a tag")
        if(self.children==None):
            raise ValueError("Parent node needs childrens")
        text=""
        for childs in self.children:
            
            text+=childs.to_html()
        return f"<{self.tag}>{text}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag} ,{self.value} , {self.children})"


