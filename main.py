import argparse
import datetime
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


def log_execution_time(task, start_time):
    """logging execution times"""
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(
        f"[{end_time.strftime('%Y-%m-%d %H:%M:%S')}] Task {task} completed in {elapsed_time.total_seconds():.6f} seconds.")


def main():
    parser = argparse.ArgumentParser(description="Process a text file to count lines or search for a keyword.")
    parser.add_argument("file", help="Path to the text file", default="data.txt", nargs="?")
    parser.add_argument("-s", "--search", help="Keyword to search for in the file", metavar="KEYWORD")

    args = parser.parse_args()
    file_path = args.file

    start_time = datetime.datetime.now()

    if args.search:
        results = search_keyword(file_path, args.search)
        if results:
            print(f"Lines containing '{args.search}':")
            for result in results:
                print(result)
        else:
            print(f"No matches found for '{args.search}'.")
        log_execution_time(f"Searching for '{args.search}'", start_time)
    else:
        num_lines = count_lines(file_path)
        if num_lines is not None:
            print(f"Total lines: {num_lines}")
        log_execution_time("Counting lines", start_time)


# program will count data.txt lines, unless search keyword is given as a param
if __name__ == "__main__":
    main()
