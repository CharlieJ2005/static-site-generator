import os
import shutil
from textnode import TextType, TextNode


def main():
    copy_dir("static", "public")


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


if __name__ == "__main__":
    main()
