class HTMLNode:
    def __init__(self, tag=None, value=None , children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def aprops_to_html(self):
        return 
    
    def __repr__(self) -> str:
        print(self.)



"""
The HTMLNode class should have 4 data members set in the constructor:
tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. 
For example, a link (<a> tag) might have {"href": "https://www.google.com"}
Perhaps counterintuitively, every data member should be optional and default to None:
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
Add a to_html(self) method. For now, it should just raise a NotImplementedError.
 Child classes will override this method to render themselves as HTML.
Add aprops_to_html(self) method. It should return a string that represents the HTML attributes of the node. For example, if self.props is:
"""