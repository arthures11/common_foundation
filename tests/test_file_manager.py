import os
import pytest
from main import FileManager, SearchResult

TEST_FILE = "test_data.txt"


@pytest.fixture
def file_manager():
    """fixture to create a FileManager instance with a test file"""
    with open(TEST_FILE, "w", encoding="utf-8") as f:
        f.writelines([
            "test\n",
            "test file\n",
            "week3_python\n",
            "hey hey hey test\n"
        ])
    yield FileManager(TEST_FILE)
    os.remove(TEST_FILE)


def test_count_lines(file_manager):
    """testing line counting"""
    assert file_manager.count_lines() == 4


def test_search_keyword_found(file_manager):
    """testing keyword when matches are found"""
    results = file_manager.search_keyword("hey")
    assert len(results) == 1
    assert results[0].text == "hey hey hey test"


def test_search_keyword_not_found(file_manager):
    """testing keyword with no matches found"""
    results = file_manager.search_keyword("NOTHING")
    assert len(results) == 0


def test_write_data(file_manager):
    """testing writing new data to the file"""
    new_data = ["new stuff\n", "linia_druga123\n"]
    file_manager.write_data(new_data)

    assert file_manager.count_lines() == 2
    results = file_manager.search_keyword("new")
    assert len(results) == 1
    assert results[0].text == "new stuff"
