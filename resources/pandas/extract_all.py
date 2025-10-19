#!/usr/bin/env python3
"""Extract Pandas tutorials from downloaded HTML files."""

import re
import html as html_module
from pathlib import Path

def clean_html(text):
    """Remove HTML tags and decode entities."""
    # Convert inline formatting
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

    # Remove all other HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Decode HTML entities
    text = html_module.unescape(text)

    # Clean whitespace
    text = ' '.join(text.split())

    return text.strip()

def extract_content(html_file, title):
    """Extract tutorial content from HTML file."""
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        return f"# {title}\n\n*Content not available - file not found*\n"

    markdown = f"# {title}\n\n"

    # Find main content area - extract between h2 tags
    # Start after navigation, look for actual tutorial h2s
    sections = re.findall(r'<h2>(.*?)</h2>(.*?)(?=<h2>|<div class="w3-clear nextprev">)', content, re.DOTALL)

    for header, section_content in sections:
        header_clean = clean_html(header)

        # Skip navigation headers
        if any(skip in header_clean.lower() for skip in ['all our services', 'get certified', 'color picker']):
            continue

        markdown += f"## {header_clean}\n\n"

        # Extract paragraphs
        paras = re.findall(r'<p>(.*?)</p>', section_content, re.DOTALL)
        for para in paras:
            para_clean = clean_html(para)
            if para_clean and len(para_clean) > 10 and 'Try it Yourself' not in para_clean:
                markdown += f"{para_clean}\n\n"

        # Extract lists
        lists = re.findall(r'<ul>(.*?)</ul>', section_content, re.DOTALL)
        for ul in lists:
            items = re.findall(r'<li>(.*?)</li>', ul, re.DOTALL)
            for item in items:
                item_clean = clean_html(item)
                if item_clean:
                    markdown += f"- {item_clean}\n"
            if items:
                markdown += "\n"

        # Extract code examples
        codes = re.findall(r'<div class="w3-example[^"]*">.*?<div class="w3-code[^"]*">(.*?)</div>',
                          section_content, re.DOTALL)
        for code in codes:
            code_clean = re.sub(r'<span[^>]*>', '', code)
            code_clean = re.sub(r'</span>', '', code_clean)
            code_clean = html_module.unescape(code_clean).strip()
            if code_clean and len(code_clean) > 5:
                markdown += f"```python\n{code_clean}\n```\n\n"

        # Extract notes/panels
        notes = re.findall(r'<div class="w3-panel[^"]*ws-note[^"]*">(.*?)</div>\s*</div>',
                          section_content, re.DOTALL)
        for note in notes:
            note_clean = clean_html(note)
            if note_clean and len(note_clean) > 15:
                markdown += f"> {note_clean}\n\n"

        markdown += "---\n\n"

    return markdown

# Define all tutorials
tutorials = [
    ('/tmp/pandas_getting_started.html', '02-pandas_getting_started.md', 'Pandas Getting Started'),
    ('/tmp/pandas_series.html', '03-pandas_series.md', 'Pandas Series'),
    ('/tmp/pandas_dataframes.html', '04-pandas_dataframes.md', 'Pandas DataFrames'),
    ('/tmp/pandas_csv.html', '05-pandas_csv.md', 'Pandas - Read CSV'),
    ('/tmp/pandas_json.html', '06-pandas_json.md', 'Pandas - Read JSON'),
    ('/tmp/pandas_analyzing.html', '07-pandas_analyzing.md', 'Pandas - Analyzing DataFrames'),
    ('/tmp/pandas_cleaning.html', '08-pandas_cleaning.md', 'Pandas - Cleaning Data'),
    ('/tmp/pandas_cleaning_empty_cells.html', '09-pandas_cleaning_empty_cells.md', 'Pandas - Cleaning Empty Cells'),
    ('/tmp/pandas_cleaning_wrong_format.html', '10-pandas_cleaning_wrong_format.md', 'Pandas - Cleaning Wrong Format'),
    ('/tmp/pandas_cleaning_wrong_data.html', '11-pandas_cleaning_wrong_data.md', 'Pandas - Cleaning Wrong Data'),
    ('/tmp/pandas_cleaning_duplicates.html', '12-pandas_cleaning_duplicates.md', 'Pandas - Removing Duplicates'),
    ('/tmp/pandas_correlations.html', '13-pandas_correlations.md', 'Pandas - Correlations'),
    ('/tmp/pandas_plotting.html', '14-pandas_plotting.md', 'Pandas - Plotting'),
]

# Output directory
output_dir = Path(__file__).parent
all_content = []
outline_data = [{'number': '01', 'title': 'Pandas Introduction', 'sections': ['What is Pandas?', 'Why Use Pandas?', 'What Can Pandas Do?', 'Where is the Pandas Codebase?']}]

print("Processing Pandas tutorials...\n")

for html_file, md_file, title in tutorials:
    print(f"Processing {md_file}...")
    markdown = extract_content(html_file, title)

    # Save file
    output_path = output_dir / md_file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"  Created {md_file} ({len(markdown)} bytes)")

    # Collect for complete tutorial
    all_content.append(markdown)

    # Extract outline
    lines = markdown.split('\n')
    h2s = [l.replace('## ', '').replace('---', '').strip() for l in lines if l.startswith('## ')]
    h2s = [s for s in h2s if s]  # Remove empty
    outline_data.append({
        'number': md_file.split('-')[0],
        'title': title,
        'sections': h2s
    })

# Add first file content
with open(output_dir / '01-pandas_intro.md', 'r') as f:
    all_content.insert(0, f.read())

print("\nCreating combined files...\n")

# Create complete tutorial
complete_path = output_dir / 'pandas_complete_tutorial.md'
with open(complete_path, 'w', encoding='utf-8') as f:
    f.write("# Pandas Complete Tutorial\n\n")
    f.write("*Complete W3Schools Pandas Tutorial - All Sections Combined*\n\n")
    f.write("This comprehensive guide covers all aspects of Pandas, from basic introduction ")
    f.write("to advanced data analysis and visualization.\n\n")
    f.write("**Source:** W3Schools Python Pandas Tutorial\n\n")
    f.write("---\n\n")
    f.write('\n\n'.join(all_content))

print(f"Created pandas_complete_tutorial.md")

# Create outline
outline_path = output_dir / 'pandas_tutorial_outline.md'
with open(outline_path, 'w', encoding='utf-8') as f:
    f.write("# Pandas Tutorial Outline\n\n")
    f.write("*W3Schools Pandas Tutorial - Complete Topic Overview*\n\n")
    f.write("This outline provides a quick reference to all topics covered in the Pandas tutorial series.\n\n")
    f.write("---\n\n")

    for item in outline_data:
        f.write(f"### {item['number']}. {item['title']}\n\n")
        if item['sections']:
            for section in item['sections']:
                f.write(f"   - {section}\n")
            f.write('\n')

print(f"Created pandas_tutorial_outline.md")
print("\nDone! All files created successfully.")
