#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Configuration
BLOG_DIR = "blog"  # Path to your blog directory
README_PATH = "README.md"  # Path to your main README
RECENTS_START_MARKER = "<!--RECENTS_START -->"
RECENTS_END_MARKER = "<!--RECENTS_END -->"

def extract_title_and_date(file_path):
    """Extract title and date from markdown file content"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Try to find title from frontmatter or first heading
    title_match = re.search(r'^# (.*)', content, re.MULTILINE) or re.search(r'title: ["\'](.*)["\']', content)
    title = title_match.group(1) if title_match else os.path.basename(file_path).replace('.md', '').replace('-', ' ').title()
    
    # Try to find date from frontmatter or filename
    date_match = re.search(r'date: ["\'](.*)["\']', content)
    if date_match:
        date_str = date_match.group(1)
        try:
            date = datetime.strptime(date_str.split('T')[0], '%Y-%m-%d')
        except ValueError:
            date = None
    else:
        # Try to extract date from filename (e.g., 2023-05-15-blog-title.md)
        filename = os.path.basename(file_path)
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            try:
                date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
            except ValueError:
                date = None
        else:
            date = None
    
    return title, date

def generate_recents():
    # Find all markdown files in blog directory
    blog_files = []
    for file in os.listdir(BLOG_DIR):
        if file.endswith('.md') and not (file.startswith('README') or file.startswith('DRAFT')):
            file_path = os.path.join(BLOG_DIR, file)
            title, date = extract_title_and_date(file_path)
            blog_files.append({
                'file': file,
                'title': title,
                'date': date
            })
    
    # Sort by date (newest first)
    blog_files.sort(key=lambda x: (x['date'] is None, x['date'] if x['date'] else ''), reverse=True)

    # Generate TOC
    toc = f"{RECENTS_START_MARKER}\n## Recent Posts\n\n"
    for entry in blog_files:
        date_str = entry['date'].strftime('%Y-%m-%d') if entry['date'] else ''
        if date_str:
            toc += f"- [{entry['title']}]({BLOG_DIR}/{entry['file']}) - {date_str}\n"
        else:
            toc += f"- [{entry['title']}]({BLOG_DIR}/{entry['file']})\n"
    toc += f"{RECENTS_END_MARKER}"
    
    # Update README
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Replace TOC section if markers exist
    if RECENTS_START_MARKER in readme_content and RECENTS_END_MARKER in readme_content:
        pattern = f"{RECENTS_START_MARKER}.*?{RECENTS_END_MARKER}"
        new_readme = re.sub(pattern, toc, readme_content, flags=re.DOTALL)
    else:
        # If markers don't exist, append TOC to the end
        new_readme = readme_content + "\n\n" + toc
    
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print(f"✅ Updated table of contents in {README_PATH}")

if __name__ == "__main__":
    generate_recents()