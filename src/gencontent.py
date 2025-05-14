import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages from markdown files
    """
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir_path, exist_ok=True)
    
    print(f"Processing directory: {dir_path_content}")
    
    # Process all entries in the content directory
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        
        if os.path.isdir(entry_path):
            # It's a directory, so recursively process it
            print(f"Found directory: {entry}")
            dest_subdir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(entry_path, template_path, dest_subdir)
        elif entry.endswith('.md'):
            # It's a markdown file, generate HTML
            print(f"Found markdown file: {entry}")
            
            # Create corresponding HTML file path
            dest_html_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))
            
            # If it's an index.md file, we want index.html
            if entry == 'index.md':
                print(f"Processing index file: {entry_path}")
                dest_html_path = os.path.join(dest_dir_path, 'index.html')
            
            print(f"Generating HTML: {entry_path} -> {dest_html_path}")
            generate_page(entry_path, template_path, dest_html_path)


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")