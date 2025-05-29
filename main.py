import sys
from stats import *

def main(file_path):
    chars = sorted_list(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(file_path)} total words")
    print("--------- Character Count -------")
    for i in range(0,len(chars)):
        dic = chars[i]
        char = dic["char"]
        num = dic["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

if len(sys.argv) < 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])