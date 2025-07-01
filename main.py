from stats import count_words, count_letters, sort_letters
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]    
    contents = get_book_text(book_path)
    num_words = count_words(contents)
    letters = count_letters(contents)
    sorted_letters = sort_letters(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_letters:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()