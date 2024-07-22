import os

from textnode import TextNode
from copystatic import copy_contents
from site_generator import generate_pages_recursive

def main():
    new_node = TextNode('this is a text node', 'bold', 'https://www.boot.dev')
    print(new_node)

    copy_contents("/home/colewortman/workspace/github.com/colewortman/static-site-project/static",
     "/home/colewortman/workspace/github.com/colewortman/static-site-project/public")

    generate_pages_recursive("content/", "template.html", "public/")

main()