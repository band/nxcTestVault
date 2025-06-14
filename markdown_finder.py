#!/usr/bin/env python3

import logging, os
log_level = os.environ.get('LOGLEVEL', 'WARNING').upper()

logging.basicConfig(
    level=getattr(logging, log_level, 'WARNING'),
    format="%(asctime)s - %(name)s - %(levelname)s: %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger('markpub_bluesky_posting')

import re
import os
from pathlib import Path
from urllib.parse import urlparse

def get_filename():
    try:
        filename = input("Enter the Markdown file name: ").strip()
        if (filename.startswith('"') and filename.endswith('"')) or (filename.startswith("'") and filename.endswith("'")):
            filename = filename[1:-1]
#            logger.debug(f"filename: {filename}")
        return filename
    except KeyboardInterrupt:
        print("\nCTRL-C detected; exiting.")
        exit()

def find_markdown_from_url(url):
    """
    Find markdown files matching a pattern derived from a URL.
    
    Args:
        url (str): The URL to extract the base name from
        
    Returns:
        list: List of matching markdown file paths
    """
    # Extract the base name from URL (filename without extension)
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    base = os.path.splitext(filename)[0]
    logger.debug(f"filename: {filename}, base: {base}")
    # Extract alphanumeric words
    words = re.findall(r'[a-zA-Z0-9-]+', base)
    logger.debug(f"words: {words}")
    
    if not words:
        return []
    
    # Build the pattern - words separated by optional special characters
    pattern_parts = []
    for i, word in enumerate(words):
        pattern_parts.append(word)
        if i < len(words) - 1:  # Not the last word
            pattern_parts.append(r'[ _?\#%"]*')
    
    pattern = ''.join(pattern_parts) + r'\.md$'
    
    # Find matching markdown files
    matches = []
    for md_file in Path('.').rglob('*.md'):
        # Skip hidden directories (those starting with .)
        if any(part.startswith('.') for part in md_file.parts):
            continue
            
        # Check if filename matches the pattern
        if re.search(f'(^|/){pattern}', str(md_file), re.IGNORECASE):
            logger.debug(f"md_file: {md_file}")
            matches.append(str(md_file))
    
    return matches

# Example usage

def main() :
    test_url = get_filename()
#    test_url = "https://nxctestvault.netlify.app/margalit_-_ethics_of_memory"
    logger.debug(f"test_url: {test_url}")
    results = find_markdown_from_url(test_url)
    for result in results:
        print(result)

if __name__ == "__main__":
    exit(main())

