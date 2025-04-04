from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil


def main():
    node = TextNode("This is some text", TextType.LINK, "https://example.com")
    print(node)


def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    items = os.listdir(source_dir)
    for item in items:
        source_item_path = os.path.join(source_dir, item)
        dest_item_path = os.path.join(dest_dir, item)
        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, dest_item_path)
            print(f"copied file: {source_item_path} to {dest_item_path}")
        else:
            os.mkdir(dest_item_path)
            print(f"created Directory: {dest_item_path}")
            copy_static(source_item_path, dest_item_path)
            


    







main()


