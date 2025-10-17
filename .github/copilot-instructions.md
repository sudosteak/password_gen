# GitHub Copilot Instructions for password_gen

## Project Overview

This is a simple Python password generator that creates secure passphrases and usernames using a wordlist-based approach.

## Project Structure

```
password_gen/
├── main.py           # Entry point - CLI interface for password/username generation
├── passwd_gen.py     # Password generation logic
├── usr_gen.py        # Username generation logic
├── assets/
│   └── wordlist.txt  # Word list used for generation
└── .github/
    └── ISSUE_TEMPLATE/ # Issue templates for bugs and features
```

## Code Style and Standards

### Python Standards
- Follow PEP 8 style guidelines
- Use Python 3.x compatible syntax
- Keep functions simple and focused on single responsibility
- Use descriptive variable names
- Handle exceptions gracefully with try-except blocks

### File Paths
- Use relative paths for asset files (e.g., `./assets/wordlist.txt`)
- Ensure file operations include proper error handling for missing files

## Key Functionality

### Password Generation (`passwd_gen.py`)
- Generates passphrases from multiple random words
- Appends random digits (0-9) to each word
- Joins words with hyphens
- Prompts user for number of words to include

### Username Generation (`usr_gen.py`)
- Generates usernames from a single random word
- Appends random 4-digit number (0-9999)
- Returns single username string

### Main Interface (`main.py`)
- Provides interactive CLI menu
- Options: (u)sername, (p)assphrase, (q)uit
- Calls appropriate generator based on user choice

## Testing Considerations

When adding tests:
- Test with valid and invalid inputs
- Test file reading operations
- Test random generation produces expected formats
- Mock user input for CLI testing
- Ensure wordlist.txt exists and is accessible

## Future Enhancements (from TODO)

- Add CLI arguments for customization
- Write unit tests
- Add comprehensive documentation
- Consider optional GUI (low priority)

## Dependencies

- Python 3.x standard library only
- `random` module for generating passwords/usernames
- No external package dependencies required

## Common Tasks

### Running the Application
```bash
python3 main.py
```

### Adding New Features
- Keep the simple, modular structure
- Add new generator functions as separate modules
- Update main.py menu to include new options
- Maintain backward compatibility with existing functions

## Important Notes

- The project uses a wordlist file at `assets/wordlist.txt` - ensure it exists
- User input validation should be improved for production use
- Consider input sanitization for security
- Password strength depends on wordlist size and quality
