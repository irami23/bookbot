import stats
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_contents = get_book_text(sys.argv[1])
        num_words = stats.get_num_words(book_contents)
        #print(f'{num_words} words found in the document')
        #print(stats.get_num_char(book_contents))
        char_cnt = stats.sorted_list(stats.get_num_char(book_contents))
        char_cnt.sort(reverse=True, key=stats.sort_on)
        #print(char_cnt)
        print(
        f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')
        for i in char_cnt:
            print(f'{i["char"]}: {i["cnt"]}')
        print("============= END ===============")

main()