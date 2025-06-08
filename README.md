Bookbot
A Python CLI tool for analyzing text files, counting words and letter frequencies in novels like Frankenstein, Pride and Prejudice, and Moby-Dick from Project Gutenberg. Built as a guided project for Boot.dev’s Backend Developer Path, this tool showcases file I/O, dictionary manipulation, and CLI argument parsing.
Features

Processes any text file provided via CLI argument (python3 main.py books/frankenstein.txt).
Counts total words using Python’s .split() method.
Tabulates letter frequencies (a-z, case-insensitive) with a dictionary.
Generates a formatted report displaying word count and letter frequencies.
Handles invalid inputs with a usage message and exit code (sys.exit(1)).
Ignores non-code files (e.g., books, virtual env) via .gitignore.

Setup

Clone the repository:git clone https://github.com/pizza-tech-ops/bookbot
cd bookbot


Create and activate a virtual environment:python3 -m venv .venv
source .venv/bin/activate


Add books to the books/ directory (ignored by .gitignore):
Download plain text UTF-8 files from Project Gutenberg


Save as books/frankenstein.txt, books/prideandprejudice.txt, books/mobydick.txt.


Run the tool:python3 main.py books/frankenstein.txt



Example Output
--- Begin report of books/frankenstein.txt ---
Found 75767 total words

Each letter was found the following number of times:
a: 25894
b: 4868
c: 9011
...
z: 235
--- End report ---

Files

main.py: Entry point for the CLI tool, handles sys.argv for file paths, and orchestrates report generation.
stats.py: Contains count_words and count_characters functions for text analysis.
.gitignore: Excludes .venv/, books/, and __pycache__/.
README.md: Project overview and setup instructions.

Development

Built with Python 3.8+ in a virtual environment.
Uses standard libraries: sys for CLI arguments, file I/O for text processing.
Tested with Frankenstein (75,767 words), Pride and Prejudice (130,410 words), and Moby-Dick (~215,838 words).
Commit history reflects iterative development, from initial setup to CLI enhancements.

Author
Pizza, a backend developer in training, transitioning from a decade of ESL teaching and novel-writing to conquer code. Passionate about crafting tools that analyze and tell stories through data. Connect on GitHub or LinkedIn.
Built with grit, late-night pizza, and a ton of commits for Boot.dev, June 2025.
   
