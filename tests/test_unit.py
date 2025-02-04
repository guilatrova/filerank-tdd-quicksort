import pytest

from main import (
    generate_output,
    process_input,
    process_rank,
    rank_files,
    trim_search_words,
)


@pytest.fixture()
def mocked_files(mocker):
    return {
        "/home/mocked-folder/file1.txt": "content of file 1",
        "/home/mocked-folder/file2.txt": "content of file 2",
        "/home/mocked-folder/file3.txt": "yet another content",
        "/home/mocked-folder/file4.txt": "one more content",
    }


def get_filename(index):
    return f"/home/mocked-folder/file{index}.txt"


def test_trim_search_words():
    trimmed = trim_search_words(["to", "be", "or", "not", "to", "be"])
    assert len(trimmed) == 4


def test_rank_files_100(mocked_files):
    words = ["content"]
    results = rank_files(words, mocked_files)

    assert len(results) == 4
    for file in mocked_files.keys():
        assert file in results
        assert results[file] == 100


def test_rank_files_100_0(mocked_files):
    words = ["file"]

    results = rank_files(words, mocked_files)
    assert results[get_filename(1)] == 100
    assert results[get_filename(2)] == 100
    assert results[get_filename(3)] == 0
    assert results[get_filename(4)] == 0


def test_rank_files_multiple_words_100_50(mocked_files):
    words = ["content", "file"]

    results = rank_files(words, mocked_files)
    assert results[get_filename(1)] == 100
    assert results[get_filename(2)] == 100
    assert results[get_filename(3)] == 50
    assert results[get_filename(4)] == 50


def test_rank_counts_the_whole_word(mocked_files):
    words = ["on"]

    results = rank_files(words, mocked_files)
    assert results[get_filename(1)] == 0
    assert results[get_filename(2)] == 0
    assert results[get_filename(3)] == 0
    assert results[get_filename(4)] == 0


def test_rank_counts_100_when_content_is_word():
    words = ["on"]

    results = rank_files(words, {"file1.txt": "on"})

    assert results["file1.txt"] == 100


def test_process_input():
    userinput = "my list of words"
    expected = ["my", "list", "of", "words"]

    result = process_input(userinput)

    assert result == expected


def test_generate_output():
    inputs = [
        {"filename": "long/long/path/file1.txt", "value": 100},
        {"filename": "long/long/path/file2.txt", "value": 15.06},
        {"filename": "long/long/path/file3.txt", "value": 73.32},
        {"filename": "long/long/path/file4.txt", "value": 0},
    ]

    assert generate_output(inputs[0]) == "file1.txt - 100.00%"
    assert generate_output(inputs[1]) == "file2.txt - 15.06%"
    assert generate_output(inputs[2]) == "file3.txt - 73.32%"
    assert generate_output(inputs[3]) == "file4.txt - 0.00%"


def test_sort_results_by_rank():
    inputs = {"file1.txt": 10, "file2.txt": 30, "file3.txt": 30.05, "file4.txt": 80}

    expected_order = [80, 30.05, 30, 10]

    results = process_rank(inputs)

    for i in range(len(expected_order)):
        assert results[i]["value"] == expected_order[i]


def test_sort_results_returns_max_top_10():
    inputs = {
        "file2.txt": 30,  # seventy
        "file1.txt": 2.75,
        "file3.txt": 30.05,  # sixty
        "file4.txt": 80,  # fifth
        "file6.txt": 96.2,  # fourth
        "file7.txt": 99,  # second
        "file9.txt": 22,  # eighty
        "file10.txt": 8.14,  # ninety
        "file11.txt": 3.99,  # tenth
        "file8.txt": 100,  # first
        "file12.txt": 3,
        "file13.txt": 1,
        "file5.txt": 97.1,  # third
    }

    expected_order = [100, 99, 97.1, 96.2, 80, 30.05, 30, 22, 8.14, 3.99]

    results = process_rank(inputs)

    assert len(expected_order) == len(results)
    for i in range(len(expected_order)):
        assert results[i]["value"] == expected_order[i]
