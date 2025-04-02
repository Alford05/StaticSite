from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i  % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        current_text = old_node.text
        current_result = []
        while True:
            image_info = extract_markdown_images(current_text)
            if image_info is None or len(image_info) != 3:
                if current_text:
                    current_result.append(TextNode(current_text, TextType.TEXT))
                break
            alt, link, markdown = image_info
            sections = current_text.split(markdown, 1)
            if sections[0]:
                current_result.append(TextNode(sections[0], TextType.TEXT))
            current_result.append(TextNode(alt, TextType.IMAGE, link))
            current_text = sections[1]
        result.extend(current_result)
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        current_text = old_node.text
        current_result = []
        while True:
            link_info = extract_markdown_links(current_text)
            if link_info is None:
                if current_text:
                    current_result.append(TextNode(current_text, TextType.TEXT))
                break
            text, url, markdown = link_info
            sections = current_text.split(markdown, 1)
            if sections[0]:
                current_result.append(TextNode(sections[0], TextType.TEXT))
            current_result.append(TextNode(text, TextType.LINK, url))
            current_text = sections[1]
        result.extend(current_result)
    return result


        

     
        

    
        

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

