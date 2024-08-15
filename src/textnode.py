class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,node):
        if (self.text == node.text and self.text_type == node.text_type
            and self.url == node.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    dum = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(dum)

