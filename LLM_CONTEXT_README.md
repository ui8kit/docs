# LLM Context Generator

Generate `llms-full.txt` - a complete documentation file for use as LLM context.

## Overview

This tool combines all markdown files from the `docs/` directory into a single, organized file that can be used as context for Large Language Models (LLMs) like Claude, ChatGPT, etc.

## Available Scripts

We provide three versions of the script:

### 1. JavaScript/Node.js (`scripts/generate-llm-context.js`)

**Requirements:** Node.js installed

**Usage:**
```bash
node scripts/generate-llm-context.js
```

**Features:**
- Cross-platform (Windows, Mac, Linux)
- No additional dependencies
- Executable with shebang (`#!/usr/bin/env node`)

### 2. Python (`scripts/generate-llm-context.py`)

**Requirements:** Python 3.6+

**Usage:**
```bash
python scripts/generate-llm-context.py
# or
python3 scripts/generate-llm-context.py
```

**Features:**
- Cross-platform support
- Standard library only (no dependencies)
- Executable with shebang

### 3. Bash Shell (`scripts/generate-llm-context.sh`)

**Requirements:** Bash shell (Unix/Mac/Linux)

**Usage:**
```bash
bash scripts/generate-llm-context.sh
# or make it executable first
chmod +x scripts/generate-llm-context.sh
./scripts/generate-llm-context.sh
```

**Features:**
- Optimized for Unix-like systems
- Colored output for better readability
- Fastest execution

---

## Quick Start

### On Windows

```bash
node scripts/generate-llm-context.js
```

### On Mac/Linux

```bash
./scripts/generate-llm-context.sh
# or
python3 scripts/generate-llm-context.py
```

---

## Output

All scripts generate the same output file:

**Location:** `llms-full.txt` (in project root)

**Structure:**
```
# UI8Kit/Core - Complete Documentation for LLM Context
# ========================================================================
# Generated: 2024-11-03T12:34:56Z
# Total Files: 23
# ========================================================================

## TABLE OF CONTENTS

1. README.md
2. 01-overview/README.md
3. 02-getting-started/README.md
... (complete index)

# ========================================================================
# DOCUMENTATION CONTENT
# ========================================================================

# FILE 1: README.md
# ========================================================================
(content of README.md)

# FILE 2: 01-overview/README.md
# ========================================================================
(content of 01-overview/README.md)

... (all files included)
```

---

## File Size

Expected output size: **500KB - 2MB**
- Contains 23 markdown files
- Complete documentation with examples
- Ready for LLM context

---

## Usage in LLM Tools

### Cursor/VSCode with Claude

1. Generate the file: `node scripts/generate-llm-context.js`
2. Open `llms-full.txt`
3. In Cursor:
   - Use `Cmd+L` (Mac) or `Ctrl+L` (Windows) to open composer
   - Paste `llms-full.txt` content
   - Ask questions about the library

### ChatGPT

1. Generate the file: `node scripts/generate-llm-context.js`
2. Go to https://chat.openai.com
3. In a new conversation:
   - Drag and drop `llms-full.txt` or click upload
   - Wait for processing
   - Ask questions about UI8Kit/Core

### Claude API

```python
import anthropic

# Read the context file
with open('llms-full.txt', 'r') as f:
    context = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": f"{context}\n\nQuestion: How do I use the Button component?"
        }
    ]
)
print(response.content[0].text)
```

### Other LLMs

Similar approach for:
- Google Gemini
- Perplexity
- Llama-based services
- Any LLM with context window support

---

## Automation

### Add to package.json (Node.js project)

```json
{
  "scripts": {
    "generate:llm": "node scripts/generate-llm-context.js"
  }
}
```

Then run:
```bash
npm run generate:llm
```

### Add to Makefile

```makefile
.PHONY: scripts/generate-llm
scripts/generate-llm:
	node scripts/generate-llm-context.js
```

Then run:
```bash
make scripts/generate-llm
```

### Pre-commit Hook

`.git/hooks/pre-commit`:
```bash
#!/bin/bash
node scripts/generate-llm-context.js
git add llms-full.txt
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Features

✅ **Automatic file discovery** - Finds all `.md` files recursively
✅ **Logical sorting** - Orders files by section (Overview → Architecture → API → etc.)
✅ **Table of contents** - Quick reference of all included files
✅ **Clear separators** - Easy to parse and navigate
✅ **Metadata** - Generation timestamp and file count
✅ **Cross-platform** - Works on Windows, Mac, Linux
✅ **No dependencies** - Pure Node.js/Python/Bash
✅ **Error handling** - Validates directory existence
✅ **File size reporting** - Shows output file size

---

## Troubleshooting

### Script not found
```bash
# Check if scripts exist
ls -la scripts/generate-llm-context.*
```

### Permission denied on bash script
```bash
chmod +x scripts/generate-llm-context.sh
./scripts/generate-llm-context.sh
```

### Node.js not installed
```bash
# Install Node.js from https://nodejs.org
# Then try again
node scripts/generate-llm-context.js
```

### Python not found
```bash
# On Mac with Homebrew
brew install python3

# On Ubuntu/Debian
sudo apt-get install python3

# Then try
python3 scripts/generate-llm-context.py
```

### File size too large
The file is typically 500KB-2MB:
- This fits in most LLM context windows
- Can be used as supplementary context
- Consider splitting if needed for specific LLM

---

## Performance

Typical execution times:
- **Node.js:** < 100ms
- **Python:** < 200ms
- **Bash:** < 50ms

File I/O dominated - dependent on disk speed.

---

## Integration Examples

### Auto-generate on documentation update

**Using npm:**
```bash
# In package.json
{
  "scripts": {
    "postinstall": "node scripts/generate-llm-context.js",
    "prebuild": "node scripts/generate-llm-context.js"
  }
}
```

### GitHub Actions

`.github/workflows/scripts/generate-llm-context.yml`:
```yaml
name: Generate LLM Context

on:
  push:
    paths:
      - 'docs/**'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: node scripts/generate-llm-context.js
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "chore: regenerate llms-full.txt"
```

---

## Contributing

When adding new documentation:
1. Add markdown files to `docs/`
2. Run: `node scripts/generate-llm-context.js`
3. Commit both the `.md` files and `llms-full.txt`

---

## Tips for Best Results

1. **Use with Cursor Composer**
   - Best for interactive code generation
   - Can reference specific pages from context

2. **Include in bug reports**
   - Paste relevant sections from `llms-full.txt`
   - Helps LLM understand your use case

3. **Update regularly**
   - Regenerate when docs change
   - Keep in sync with documentation

4. **Version control**
   - Commit `llms-full.txt` to git
   - Track documentation changes

---

## Support

For issues or questions:
1. Check that `docs/` directory exists
2. Verify all `.md` files are readable
3. Ensure sufficient disk space for output
4. Check tool-specific documentation

---

**Created:** November 3, 2024  
**Last Updated:** 2024-11-03  
**Status:** ✅ Production Ready
