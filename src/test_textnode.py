import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_none(self):
        node = TextNode("test", "bold", None)
        node2 = TextNode("test","bold", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("test", 'bold')
        node2 = TextNode("fake","bold")
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()


# Add some tests by adding methods to the TestTextNode class and using self.assertEqual to verify that the TextNode class works as expected.
# Add even more tests (at least 3 in total) to check various edge cases, like when the url property is None, or when the text_type property is different. You'll want to make sure that when properties are different, the TextNode objects are not equal.
# When you're satisfied that your class is behaving as expected, move on.