import os

from markdown_blocks import markdown_to_html_node, extract_title
from htmlnode import HTMLNode

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        contents = f.read()
    
    with open(template_path, 'r') as tf:
        template_contents = tf.read()

    html_content =  markdown_to_html_node(contents).to_html()
    title = extract_title(contents)

    final_html = template_contents.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as df:
        df.write(final_html)
        
