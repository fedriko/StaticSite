import unittest

from htmlnode import *
from utilityFunctions import *
from textnode import *

class test_split_node(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected=[
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
             TextNode(" word", text_type_text),
                ]
        self.assertEqual(new_nodes,expected)
        
    def test_eq2(self):
        node = TextNode("This is text with a **code block** word", text_type_text)
        node2 = TextNode("The world",text_type_italic)
        node3 = TextNode("This **is** the light", text_type_text)
        new_nodes = split_nodes_delimiter([node,node2,node3], "**", text_type_bold)
        expected=[
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_bold),
                TextNode(" word", text_type_text),
                TextNode("The world", text_type_italic),
                TextNode("This ",text_type_text),
                TextNode("is",text_type_bold),
                TextNode(" the light",text_type_text)
                ]
        self.assertEqual(new_nodes,expected)
    
    def test_error(self):
        node = TextNode("This is text with a `code block word", text_type_text)
        self.assertRaises(Exception,split_nodes_delimiter,[node],'`',text_type_code)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )



        
