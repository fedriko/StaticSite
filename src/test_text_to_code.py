import unittest

from htmlnode import *
from utilityFunctions import *
from textnode import *

class TestTextCode(unittest.TestCase):
    def test_eq(self):
        text="This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        excepted=[
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
]
        result=text_to_textnodes(text)
        self.assertEqual(result,excepted)
    
    def test_eq2(self):
        markdown="# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        expected=["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(expected,markdown_to_blocks(markdown))

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    def test_block_to_block_type_eq(self):
        markdown="""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual("unordered_list",block_to_block_type(markdown))

    def test_block_to_block_type_eq_heading(self):
        markdown="# This is a heading"
        self.assertEqual("heading",block_to_block_type(markdown))
    
    def test_block_to_block_type_eq_heading2(self):
        markdown="halo # This is a heading"
        self.assertEqual("paragraph",block_to_block_type(markdown))
    
    def test_block_to_block_type_eq_heading3(self):
        markdown="###a This is a heading"
        self.assertEqual("paragraph",block_to_block_type(markdown))

    def test_block_to_block_type_eq_heading4(self):
        markdown="###This is a heading"
        self.assertEqual("paragraph",block_to_block_type(markdown))

    def test_block_to_block_type_eq_heading5(self):
        markdown="### This is a heading"
        self.assertEqual("heading",block_to_block_type(markdown))

    def test_block_to_block_type_eq_heading6(self):
        markdown="##### This is a heading"
        self.assertEqual("heading",block_to_block_type(markdown))

    def test_block_to_block_type_eq_heading7(self):
        markdown="####### This is a heading"
        self.assertEqual("paragraph",block_to_block_type(markdown))

    def test_block_to_block_type_eq_orderedlist(self):
        markdown="""1. wow
2. hey
3. cool"""
        self.assertEqual("ordered_list",block_to_block_type(markdown))
    def test_block_to_block_type_eq_orderedlist2(self):
        markdown="``` its code ```"
        self.assertEqual("code",block_to_block_type(markdown))
    
    def test_block_to_block_type_eq_quote(self):
        markdown=""">. wow
>. hey
>. cool"""
        self.assertEqual("quote",block_to_block_type(markdown))
    
    
    
       

   

    