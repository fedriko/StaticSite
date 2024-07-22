from htmlnode import *
from textnode import *
import re
import os
import shutil

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

def block_to_block_type(markdown):
    isquote=True
    isulist=True
    isolist=True
    unordered=["* ","- "]
    i=1
    head=markdown.split(" ")[0]
    if len(head)<7 and head.count("#")==len(head):
        return "heading"
    if markdown[:3]=="```" and markdown[-3:]=="```":
        return "code"
    lines=markdown.split('\n')
    for line in lines:
        if line[0]!=">" and isquote:
            isquote=False
        if not (line[0:2] in unordered) and isulist:
            isulist=False
        if (line[:3]!=f"{i}. "):
            isolist=False
        i+=1
    if isquote:
        return "quote"
    if isulist:
        return "unordered_list"
    if isolist:
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(makrdown):
    blocks= markdown_to_blocks(makrdown)
    childs=[]
    for block in blocks:
        match block_to_block_type(block):

            case "code":
                childs.append(code_to_html(block))
            
            case "heading":
                childs.append(heading_to_html(block))
            
            case "quote":
                childs.append(quote_to_html(block))
            
            case "ordered_list":
                childs.append(ordered_list_to_html(block))
            
            case "unordered_list":
                childs.append(unordered_list_to_html(block))
            case _:
                childs.append(paragraph_to_html(block))
    return ParentNode("div",children=childs)
    



        

def heading_to_html(block):
    splited_block=block.split("# ")
    number_hash=len(splited_block[0])+1
    childrens=text_to_children(splited_block[1])
    
    return ParentNode(f"h{number_hash}",children=childrens)

def code_to_html(block):
    splited_block=block.split("```")
    childrens=text_to_children(splited_block[1])
   
    return ParentNode("code",children=childrens)

    

def unordered_list_to_html(block):
    lines=block.split("\n")
    childs=[]
    for line in lines:
        childrens=text_to_children(line[2:])
      
        childs.append(ParentNode("li",children=childrens))
        
    return ParentNode("ul",children=childs)

def ordered_list_to_html(block):
    lines=block.split("\n")
    childs=[]
    for line in lines:
        childrens=text_to_children(line[3:])
        
        childs.append(ParentNode("li",children=childrens))

    return ParentNode("ol",children=childs)

def paragraph_to_html(block):
    new_input=block.replace("\n"," ")
    childrens=text_to_children(new_input)

    return ParentNode("p",children=childrens)

    
def quote_to_html(block):
    filtered_text=block.replace("> ","")
    double_filter=filtered_text.replace("\n"," ")
    childrens=text_to_children(double_filter)
  
    return ParentNode("blockquote",children=childrens)
    

def text_to_children(text):
    list_nodes=text_to_textnodes(text)
   
    return list(map(text_node_to_html_node,list_nodes))

def update_content(source,destination):
    if(not(os.path.exists(source) and os.path.exists(destination))):
        raise Exception("Source or destination does not exist")
    shutil.rmtree(destination)
    os.mkdir(destination)
    for file in os.listdir(source):
        if os.path.isfile(os.path.join(source,file)):
            shutil.copy(os.path.join(source,file),destination)
        else:
            os.mkdir(os.path.join(destination,file))
            update_content(os.path.join(source,file),os.path.join(destination,file))
def extract_title(markdown):
    lines=markdown.split("\n")
    i=0
    got_title=False
    title=""
    while(i<len(lines) and got_title==False):
        filtered_line=lines[i].strip()
        if(filtered_line==""):
            i+=1
            continue
        if(filtered_line[0:2]=="# "):
            got_title=True
            
            title=filtered_line[1:].strip()
        else:
            i+=1
    if(i>len(lines)):
        raise Exception("Title is missing")
    else:
        return title

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    text = open(from_path,'r')
    template=open(template_path)
    markdown=text.read()
    temp=template.read()
    html_string=markdown_to_html_node(markdown).to_html()
    temp=temp.replace("{{ Title }}",extract_title(markdown))
    temp=temp.replace("{{ Content }}",html_string)
    if(not os.path.exists(os.path.dirname(dest_path))):
        os.makedirs(os.path.dirname(dest_path))
    html_file=open(dest_path,'w')
    html_file.write(temp)
    text.close
    template.close
    html_file.close
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_dir=os.listdir(dir_path_content)
    for item in list_dir:
        
        if(os.path.isfile(os.path.join(dir_path_content,item))):
            if(item.split(".")[-1]=="md"):
                new=item.split(".")[0]+".html"
                generate_page(os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,new))
        else:
            generate_pages_recursive(os.path.join(dir_path_content,item),template_path,os.path.join(dest_dir_path,item))




    








    


