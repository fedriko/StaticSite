import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node=LeafNode("p", "This is a paragraph of text.")
        test="<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(),test)
    def test_eq(self):
        node=LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        test="<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(),test)
    def test_no_value(self):
        node=LeafNode("a", None, {"href": "https://www.google.com"})
        self.assertRaises(ValueError)



if __name__ == "__main__":
    unittest.main()