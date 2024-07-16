from htmlnode import *
from textnode import *
import re

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

def extract_markdown_images(text):
    images=re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text):
    links=re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return links

def split_nodes_image(old_nodes):
    new_nodes=[]
    place_holder="[PLACEHOLDER](nolink)"
    for node in old_nodes:
        if(node.text_type != text_type_text):
            new_nodes.append(node)
            continue
        node_text=node.text
        list_tuples=extract_markdown_images(node_text)
        for tuples in list_tuples:
            node_text=node_text.replace(f"![{tuples[0]}]({tuples[1]})",place_holder)
            
        splited_text=node_text.split(place_holder)
        i=0
        j=0
        while(i<len(list_tuples) or j<len(splited_text)):
            if(j<len(splited_text)):
                if(splited_text[i]==""):
                    j+=1
                else:
                    new_nodes.append(TextNode(splited_text[i],text_type_text))
                    j+=1
                
                
            if(i<len(list_tuples)):
                new_nodes.append(TextNode(list_tuples[i][0],text_type_image,list_tuples[i][1]))
                i+=1
            
            
           

    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes=[]
    place_holder="[PLACEHOLDER](nolink)"
    for node in old_nodes:
        if(node.text_type != text_type_text):
            new_nodes.append(node)
            continue
         
        node_text=node.text
        list_tuples=extract_markdown_links(node_text)
        for tuples in list_tuples:
            node_text=node_text.replace(f"[{tuples[0]}]({tuples[1]})",place_holder)
            
        splited_text=node_text.split(place_holder)
        i=0
        j=0
        while(i<len(list_tuples) or j<len(splited_text)):
            if(j<len(splited_text)):
                if(splited_text[i]==""):
                    j+=1
                else:
                    new_nodes.append(TextNode(splited_text[i],text_type_text))
                    j+=1
                
                
            if(i<len(list_tuples)):
                new_nodes.append(TextNode(list_tuples[i][0],text_type_link,list_tuples[i][1]))
                i+=1
           

    
    return new_nodes

def text_to_textnodes(text):
    full_text=TextNode(text,text_type_text)
    nodes_bold=split_nodes_delimiter([full_text],"**",text_type_bold)
    nodes_italic=split_nodes_delimiter(nodes_bold,"*",text_type_italic)
    nodes_code=split_nodes_delimiter(nodes_italic,"`",text_type_code)
    nodes_images=split_nodes_image(nodes_code)
    fnodes=split_nodes_link(nodes_images)
    return fnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

