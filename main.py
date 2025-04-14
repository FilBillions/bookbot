def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char(text)
    print(f"{num_words} words found in the document")
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
from stats import get_char

main()
