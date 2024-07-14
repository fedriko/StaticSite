import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):
    def test_eq(self):
      node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
      ideal="<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
      self.assertEqual(node.to_html(),ideal)
    
    def test_eq2(self):
        node = ParentNode(
    "p",
    [
         ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
        LeafNode(None, "its really nice here"),
        LeafNode("i", "boring day"),
        LeafNode(None, "Normal text"),
    ],
)
        ideal="<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>its really nice here<i>boring day</i>Normal text</p>"
        self.assertEqual(node.to_html(),ideal)



