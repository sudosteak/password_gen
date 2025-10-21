# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A simple Python password and username generator that creates passphrases from a wordlist. The tool generates memorable passphrases by combining random words from a dictionary file with numbers.

## Architecture

**Core Modules:**
- `main.py` - Entry point with interactive CLI menu for choosing username or passphrase generation
- `passwd_gen.py` - Passphrase generation module that creates multi-word passphrases with format: `word1-word2-...-wordN` where each word is appended with a random digit (0-8)
- `usr_gen.py` - Username generation module that creates usernames with format: `word + 4-digit number (0-9998)`
- `assets/wordlist.txt` - Dictionary file with newline-separated words used as the source for generation

**Key Design Patterns:**
- Both generators read from the same wordlist file (`./assets/wordlist.txt`)
- The wordlist is split by newlines to create a list of candidate words
- Random selection uses Python's `random` module with `random.choice()` for words and `random.randrange()` for numbers
- Passphrase generation prompts for word count and joins words with hyphens
- Username generation uses a single word with a larger numeric suffix (0-9998 range)

## Running the Application

```bash
# Run the interactive menu
python3 main.py

# Direct module usage in Python code
from passwd_gen import gen_passwd
from usr_gen import gen_usr

passphrase = gen_passwd("./assets/wordlist.txt")
username = gen_usr("./assets/wordlist.txt")
```

## Development Notes

- No external dependencies beyond Python standard library
- The wordlist file path is hardcoded as `./assets/wordlist.txt` in main.py
- Input validation exists in passwd_gen.py but has a bug: line 6 uses `or` instead of proper exception handling
- Both generators append numbers to words: passwd_gen uses 0-8, usr_gen uses 0-9998
- The main.py script runs interactively and doesn't support CLI arguments yet (per TODO list)
Always use context7 when I need code generation, setup or configuration steps, or library/API documentation. This means you should automatically use the Context7 MCP tools to resolve library id and get library docs without me having to explicitly ask.
