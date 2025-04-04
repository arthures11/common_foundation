import argparse
import datetime
import requests


class SearchResult:
    """object that will help output the searched line by a keyword and its line number"""

    def __init__(self, line_number, text):
        self.line_number = line_number
        self.text = text

    def __str__(self):  # used for printing
        return f"{self.line_number}: {self.text}"


class FileManager:
    """Manages file operations like reading, writing, and path storage."""

    def __init__(self, file_path):
        self.file_path = file_path

    def count_lines(self):
        """counting lines in the file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return sum(1 for _ in file)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None

    def search_keyword(self, keyword):
        """finds a keyword in a file and returns line number with its text"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                matches = [SearchResult(i + 1, line.strip()) for i, line in enumerate(file) if keyword in line]
            return matches
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None

    def write_data(self, data):
        """Overwrites the file with new data."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.writelines(data)


class APIClient:
    """Handles API requests to fetch random user data."""

    BASE_URL = "https://randomuser.me/api/"

    @staticmethod
    def fetch_random_users(count=10):
        """fetches random user data from API and returns a json"""
        url = f"{APIClient.BASE_URL}?results={count}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None


def log_execution_time(task, start_time):
    """logging execution times"""
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(
        f"[{end_time.strftime('%Y-%m-%d %H:%M:%S')}] Task {task} completed in {elapsed_time.total_seconds():.6f} seconds.")


def populate_data(file_manager, count=10):
    """fetches random user data from API using the HTTPClient class and writes it to the file (old data will be
    basically fully replaced) """
    start_time = datetime.datetime.now()
    api_client = APIClient()
    data = api_client.fetch_random_users(count)

    if data:
        lines = [f"{user['name']['first']} {user['name']['last']}, {user['email']}, {user['location']['country']}\n"
                 for user in data['results']]
        file_manager.write_data(lines)
        print(f"File '{file_manager.file_path}' has been populated with {count} random users.")
    log_execution_time("Populating data", start_time)


def main():
    parser = argparse.ArgumentParser(description="Process a text file to count lines or search for a keyword.")
    parser.add_argument("file", help="Path to the text file", default="data.txt", nargs="?")
    parser.add_argument("-s", "--search", help="Keyword to search for in the file", metavar="KEYWORD")
    parser.add_argument("-p", "--populate", help="Fetch random user data and overwrite the file", action="store_true")

    args = parser.parse_args()
    file_manager = FileManager(args.file)

    start_time = datetime.datetime.now()

    if args.search:
        results = file_manager.search_keyword(args.search)
        if results:
            print(f"Lines containing '{args.search}':")
            for result in results:
                print(result)
        else:
            print(f"No matches found for '{args.search}'.")
        log_execution_time(f"Searching for '{args.search}'", start_time)
    elif args.populate:
        populate_data(file_manager)
        log_execution_time(f"Populating new data to file '{file_manager.file_path}'", start_time)
    else:
        num_lines = file_manager.count_lines()
        if num_lines is not None:
            print(f"Total lines: {num_lines}")
        log_execution_time("Counting lines", start_time)


# program will count data.txt lines, unless search keyword is given as a param
if __name__ == "__main__":
    main()
