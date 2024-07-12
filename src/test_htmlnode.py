import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        str= " href=\"https://www.google.com\" target=\"_blank\""
        dic={
    "href": "https://www.google.com", 
    "target": "_blank",}
        node= HTMLNode("a","cockier",None,dic)
        self.assertEqual(str, node.props_to_html())
    
    def test_props_to_html2(self):
        str= " href=\"https://www.ana.com\" target=\"blank\""
        dic={
    "href": "https://www.ana.com", 
    "target": "blank",}
        node= HTMLNode("a","cockier",None,dic)
        self.assertEqual(str, node.props_to_html())
    
    def test_props_to_html2(self):
        str= " href=\"https://www..io\" target=\"wui\""
        dic={
    "href": "https://www..io", 
    "target": "wui",}
        node= HTMLNode("a","cockier",None,dic)
        self.assertEqual(str, node.props_to_html())
    
   
if __name__ == "__main__":
    unittest.main()