def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(bookString):
    word_list = bookString.split()
    return len(word_list)

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_contents)
    print(f'{num_words} words found in the document')

main()