from enum import Enum
import re
from htmlnode import ParentNode
from SplitNode import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            cleaned_blocks.append(stripped_block)
    return cleaned_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    pattern = r"^#{1,6} "
    if re.match(pattern, lines[0]):
        return BlockType.HEADING
    if lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE
    if lines[0].startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if lines[0].startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if lines[0].startswith("1. "):
        i = 1
        for line in lines:
            if line.startswith(f"{i}. "):
                i +=1 
            else:
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    return BlockType.PARAGRAPH
    

def markdown_to_html_node(markdown):









def block_to_html_node(block):









def text_to_children(text):







def paragraph_to_html_node(block):








def heading_to_html_node(block):





def code_to_html_node(block):







def olist_to_html_node(block):






def ulist_to_html_node(block):





def quote_to_html_node(block):


    







    
    