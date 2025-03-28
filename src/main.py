from textnode import TextNode, TextType

def main():
    node = TextNode("some text", TextType.LINK, "https://example.com")
    print(node)
