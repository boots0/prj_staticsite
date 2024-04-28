import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode('h1', 'test1', None, {"href": "https://www.google.com", "target": "_blank"})
        html_node_two = HTMLNode('h1', 'test2', ['1', '2', '3'], 
                             {"href": "https://www.google.com", "target": "_blank"})
        self.props_to_html(html_node)
        self.props_to_html(html_node_two)

if __name__ == "__main__":
    unittest.main()