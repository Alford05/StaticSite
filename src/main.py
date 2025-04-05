from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil
from markdown_blocks import markdown_to_html_node, extract_title, markdown_to_blocks, block_to_html_node
from markdown_blocks import block_to_block_type, block_to_html_node
import markdown_blocks


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
        else:
            os.mkdir(dest_item_path)
            copy_static(source_item_path, dest_item_path)
            

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding='utf-8') as markdown_file:
        markdown_content = markdown_file.read()
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(final_html)


def main():
    source_dir = "static"
    dest_dir = "public"
    copy_static(source_dir, dest_dir)
    generate_page("content/index.md", "template.html", "public/index.html")




if __name__ == "__main__":
    main()



