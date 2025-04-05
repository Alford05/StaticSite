import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file == "index.md" and root == dir_path_content:
                continue
            if file.endswith(".md"):
                content_path = os.path.join(root, file)
                rel_path = os.path.relpath(content_path, dir_path_content)
                public_path = os.path.join(dir_path_public, rel_path)
                public_path = os.path.splitext(public_path)[0] + ".html"
                generate_page(content_path, template_path, public_path)



main()

