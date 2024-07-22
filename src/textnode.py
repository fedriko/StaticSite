class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text=text
        self.text_type=text_type
        self.url=url
    def __eq__(self,object_2):
        return self.text==object_2.text and self.text_type==object_2.text_type and self.url==object_2.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
