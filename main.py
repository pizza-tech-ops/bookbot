import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def print_report(filepath):
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    letter_counts = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_letters = sorted(letter_counts.keys())
    print(f"--- Begin report of {filepath} ---")
    print(f"Found {num_words} total words")
    print("\nEach letter was found the following number of times:")
    for letter in sorted_letters:
        print(f"{letter}: {letter_counts[letter]}")
    print("--- End report ---")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print_report(filepath)

if __name__ == "__main__":
    main()
