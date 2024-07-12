import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq_2(self):
        node= TextNode("wow","","ok")
        node2= TextNode("Wow","","ok")
        self.assertNotEqual(node,node2)
    def test_eq_3(self):
        node= TextNode("Wow","","ok")
        node2= TextNode("Wow","","ok")
        self.assertEqual(node,node2)
    def test_eq_4(self):
        node= TextNode("wow","",)
        node2= TextNode("wow","",None)
        self.assertEqual(node,node2)
    def test_eq_5(self):
        node= TextNode("Allo","b","na")
        node2= TextNode("Allo","b","ok")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()