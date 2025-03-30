import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        # Create a node with href property
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        # Check if props_to_html returns expected string
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
    
    # Add more test methods here
    


    def test_image_node_props(self):
        # Create an image node with src, alt, and width properties
        img_node = HTMLNode(
            "img", 
            None, 
            None, 
            {
                "src": "https://example.com/image.jpg",
                "alt": "Example image",
                "width": "500"
            }
        )
        
        # Check if props_to_html includes all the image properties correctly
        expected_props = ' src="https://example.com/image.jpg" alt="Example image" width="500"'
        self.assertEqual(img_node.props_to_html(), expected_props)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()

