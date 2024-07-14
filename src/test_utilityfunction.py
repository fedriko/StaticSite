import unittest
from utilityFunctions import *
from textnode import TextNode
from htmlnode import *

class testUtilityFucntions(unittest.TestCase):

    def test_italic(self):
        node=TextNode("i love cacao","italic")
        result="<i>i love cacao</i>"
        teste=text_node_to_html_node(node).to_html()
        self.assertEqual(result,teste)
    
    def test_link(self):
        node=TextNode("i love cacao","link",url="www.costa_cacao.com")
        result="<a href=\"www.costa_cacao.com\">i love cacao</a>"
        teste=text_node_to_html_node(node).to_html()
        self.assertEqual(result,teste)
    
    def test_img(self):
        node=TextNode("i love cacao","image",url="caca.jpg")
        result="<img src=\"caca.jpg\" alt=\"i love cacao\"></img>"
        teste=text_node_to_html_node(node).to_html()
        self.assertEqual(result,teste)

