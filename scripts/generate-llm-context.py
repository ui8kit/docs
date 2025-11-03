#!/usr/bin/env python3

"""
Script to generate llms-full.txt
Concatenates all markdown files from docs/ directory into a single file
for use as LLM context
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Configuration
DOCS_DIR = Path(__file__).parent / 'docs'
OUTPUT_FILE = Path(__file__).parent / 'llms-full.txt'
EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__'}

def get_markdown_files(directory):
    """Recursively get all markdown files from a directory"""
    md_files = []
    
    for root, dirs, files in os.walk(directory):
        # Remove excluded directories from dirs in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    
    return sorted(md_files)

def sort_files(files):
    """Sort files in logical order based on directory structure"""
    order = {
        'README.md': 0,
        '01-overview': 1,
        '02-getting-started': 2,
        '03-architecture': 3,
        '04-api-reference': 4,
        '05-development-guide': 5,
        '06-troubleshooting': 6,
    }
    
    def get_sort_key(file_path):
        file_str = str(file_path)
        for key, value in order.items():
            if key in file_str:
                return value
        return 999
    
    return sorted(files, key=get_sort_key)

def generate_llm_context():
    """Generate the LLM context file"""
    print('📄 Generating LLM context file...\n')
    
    try:
        # Get all markdown files
        md_files = get_markdown_files(DOCS_DIR)
        md_files = sort_files(md_files)
        
        if not md_files:
            print('❌ No markdown files found in docs/ directory')
            sys.exit(1)
        
        print(f'Found {len(md_files)} markdown files:')
        for file in md_files:
            rel_path = file.relative_to(DOCS_DIR)
            print(f'  ✓ {rel_path}')
        
        # Generate content
        content = ''
        content += '# UI8Kit/Core - Complete Documentation for LLM Context\n'
        content += '# ' + '=' * 78 + '\n'
        content += f'# Generated: {datetime.now().isoformat()}\n'
        content += f'# Total Files: {len(md_files)}\n'
        content += '# ' + '=' * 78 + '\n\n'
        
        # Add table of contents
        content += '## TABLE OF CONTENTS\n\n'
        for index, file in enumerate(md_files, 1):
            rel_path = file.relative_to(DOCS_DIR)
            content += f'{index}. {rel_path}\n'
        
        content += '\n'
        content += '# ' + '=' * 78 + '\n'
        content += '# DOCUMENTATION CONTENT\n'
        content += '# ' + '=' * 78 + '\n\n'
        
        # Add all markdown content
        for index, file in enumerate(md_files, 1):
            rel_path = file.relative_to(DOCS_DIR)
            
            with open(file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            content += f'# FILE {index}: {rel_path}\n'
            content += '# ' + '=' * 78 + '\n'
            content += file_content
            content += '\n\n'
            content += '# ' + '=' * 78 + '\n\n'
        
        # Write to output file
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Get file size
        file_size = OUTPUT_FILE.stat().st_size
        size_mb = file_size / 1024 / 1024
        
        print(f'\n✅ Successfully generated {OUTPUT_FILE}')
        print(f'📊 File size: {size_mb:.2f} MB ({file_size:,} bytes)')
        print('\n💡 Usage: Use llms-full.txt for LLM context in tools like:')
        print('   - Cursor/VSCode with Claude')
        print('   - ChatGPT with file upload')
        print('   - Other LLM context windows\n')
        
    except Exception as error:
        print(f'❌ Error generating LLM context file: {error}')
        sys.exit(1)

if __name__ == '__main__':
    generate_llm_context()
