def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_of_words(file_path):
    words_number = len(str.split(get_book_text(file_path)))
    return words_number

def count_everything(file_path):
    file_contents_lower = str.lower(get_book_text(file_path))
    chars = {}
    for i in file_contents_lower:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars

def sorted_list(file_path):
    chars = count_everything(file_path)
    sorted_list = sorted(chars.items())
    return [{"char": char, "num": num} for char, num in sorted_list]
