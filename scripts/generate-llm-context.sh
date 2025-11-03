#!/bin/bash

# Script to generate llms-full.txt
# Concatenates all markdown files from docs/ directory into a single file
# for use as LLM context

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$SCRIPT_DIR/docs"
OUTPUT_FILE="$SCRIPT_DIR/llms-full.txt"

# Colors for output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if docs directory exists
if [ ! -d "$DOCS_DIR" ]; then
    echo -e "${RED}❌ Error: docs/ directory not found at $DOCS_DIR${NC}"
    exit 1
fi

echo -e "${BLUE}📄 Generating LLM context file...${NC}\n"

# Find all markdown files and sort them
md_files=$(find "$DOCS_DIR" -type f -name "*.md" | sort)
file_count=$(echo "$md_files" | wc -l)

echo "Found $file_count markdown files:"
echo "$md_files" | while read -r file; do
    rel_path="${file#$DOCS_DIR/}"
    echo -e "  ${GREEN}✓${NC} $rel_path"
done
echo ""

# Start generating content
{
    echo "# UI8Kit/Core - Complete Documentation for LLM Context"
    echo "# ================================================================================"
    echo "# Generated: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    echo "# Total Files: $file_count"
    echo "# ================================================================================"
    echo ""
    
    # Table of contents
    echo "## TABLE OF CONTENTS"
    echo ""
    i=1
    echo "$md_files" | while read -r file; do
        rel_path="${file#$DOCS_DIR/}"
        echo "$i. $rel_path"
        i=$((i + 1))
    done
    echo ""
    
    echo "# ================================================================================"
    echo "# DOCUMENTATION CONTENT"
    echo "# ================================================================================"
    echo ""
    
    # Add all markdown content
    i=1
    echo "$md_files" | while read -r file; do
        rel_path="${file#$DOCS_DIR/}"
        echo "# FILE $i: $rel_path"
        echo "# ================================================================================"
        cat "$file"
        echo ""
        echo ""
        echo "# ================================================================================"
        echo ""
        i=$((i + 1))
    done
} > "$OUTPUT_FILE"

# Get file size
file_size=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null || echo "unknown")
if [ "$file_size" != "unknown" ]; then
    size_kb=$((file_size / 1024))
    size_mb=$((size_kb / 1024))
    if [ $size_mb -gt 0 ]; then
        size_str="${size_mb}.$((size_kb % 1024))MB"
    else
        size_str="${size_kb}KB"
    fi
    echo -e "${GREEN}✅ Successfully generated $OUTPUT_FILE${NC}"
    echo -e "${BLUE}📊 File size: $size_str ($file_size bytes)${NC}"
else
    echo -e "${GREEN}✅ Successfully generated $OUTPUT_FILE${NC}"
fi

echo ""
echo -e "${BLUE}💡 Usage: Use llms-full.txt for LLM context in tools like:${NC}"
echo "   - Cursor/VSCode with Claude"
echo "   - ChatGPT with file upload"
echo "   - Other LLM context windows"
echo ""
