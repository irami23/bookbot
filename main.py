from stats import get_num_words, get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_contents)
    print(f'{num_words} words found in the document')
    print(get_num_char(book_contents))

main()