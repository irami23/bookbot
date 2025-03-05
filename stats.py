def get_num_words(bookString):
    word_list = bookString.split()
    return len(word_list)

def get_num_char(bookString):
    num_char = {}
    for char in bookString:
        if char.lower() in num_char:
            num_char[str(char.lower())] += 1
        else:
            num_char[str(char.lower())] = 1
    return num_char