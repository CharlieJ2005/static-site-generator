import os
import shutil
import sys
from block_markdown import markdown_to_html_node


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_dir("static", "docs")
    generate_pages_recursive(
        "content",
        "template.html",
        "public",
        basepath
        )


def copy_dir(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            copy_dir(src_path, dest_path)
            print(f"Copied directory: {src_path} -> {dest_path}")


def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Error: h1 header found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"Generating page from {from_path} to {dest_path} "
        f"using {template_path}"
    )
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_string)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(
        dir_path_content,
        template_path,
        dest_dir_path,
        basepath
        ):
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(content_path):
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path,
                basepath
                )
        elif os.path.isfile(content_path) and content_path.endswith(".md"):
            dest_dir = os.path.dirname(dest_path)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            dest_html_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(
                content_path,
                template_path,
                dest_html_path,
                basepath
                )


if __name__ == "__main__":
    main()
