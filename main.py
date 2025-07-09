from stats import get_word_count, get_symbol_count, get_sorted_dict
import sys

def get_book_text(path: str) -> str:
    content = ""
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list = get_sorted_dict(get_symbol_count(book_text))
    for i in sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()