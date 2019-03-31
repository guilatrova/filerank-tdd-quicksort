import pytest

from main import generate_output, process_input, rank_files, trim_search_words


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

    assert (
        generate_output(inputs[0]["filename"], inputs[0]["value"])
        == "file1.txt - 100.00%"
    )
    assert (
        generate_output(inputs[1]["filename"], inputs[1]["value"])
        == "file2.txt - 15.06%"
    )
    assert (
        generate_output(inputs[2]["filename"], inputs[2]["value"])
        == "file3.txt - 73.32%"
    )
    assert (
        generate_output(inputs[3]["filename"], inputs[3]["value"])
        == "file4.txt - 0.00%"
    )


# TODO: We should be sure we're reading .txt files
