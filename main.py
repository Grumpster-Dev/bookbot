import sys

from stats import word_count, char_count_sorted,char_count


def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    char_list = char_count_sorted(char_count(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count(text)
    print("--------- Character Count -------")
    for item in char_list: print(f'{item[0]}: {item[1]}')
  
    


main()
