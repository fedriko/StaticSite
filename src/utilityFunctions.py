from htmlnode import *
from textnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(tag="b",value=text_node.text)
        case "italic":
            return LeafNode(tag="i",value=text_node.text)
        case "code":
            return LeafNode(tag="code",value=text_node.text)
        case "link":
            return LeafNode(tag="a",value=text_node.text,props={"href":text_node.url})
        case "image":
            return LeafNode(tag="img",value="",props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise ValueError("Type not accepted")

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    
    nodes_list=[]

    for node in old_nodes:
        splited_node=node.text.split(delimiter)
        if(node.text_type!=text_type_text):
            nodes_list.append(node)
        else:
            if(len(splited_node)%2==0):
                raise Exception("No closing delimiter Found")
            for i in range(len(splited_node)):
                if(splited_node[i]==""):
                    continue
                if(i%2==0):
                    nodes_list.append(TextNode(splited_node[i],text_type_text))
                else:
                    nodes_list.append(TextNode(splited_node[i],text_type))

    return nodes_list


