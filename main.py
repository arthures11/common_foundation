import sys


class SearchResult:
    """object that will help output the searched line by a keyword and its line number"""

    def __init__(self, line_number, text):
        self.line_number = line_number
        self.text = text

    def __str__(self):  # used for printing
        return f"{self.line_number}: {self.text}"


def count_lines(file_path):
    """counting lines in the file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def search_keyword(file_path, keyword):
    """finds a keyword in a file and returns line number with its text"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            matches = [SearchResult(i + 1, line.strip()) for i, line in enumerate(file) if keyword in line]
        return matches
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


# program will count data.txt lines, unless search keyword is given as a param

if __name__ == "__main__":
    file_path = "data.txt"

    if len(sys.argv) == 1:
        num_lines = count_lines(file_path)
        if num_lines is not None:
            print(f"Total lines: {num_lines}")
    elif len(sys.argv) == 2:
        keyword = sys.argv[1]
        results = search_keyword(file_path, keyword)
        if results:
            print(f"Lines containing '{keyword}':")
            for result in results:
                print(result)
        else:
            print(f"No matches found for '{keyword}'.")
