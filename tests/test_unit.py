import pytest

from main import rank_files, trim_search_words


@pytest.fixture()
def mocked_files(mocker):
    return {
        "/home/mocked-folder/file1.txt": "content of file 1",
        "/home/mocked-folder/file2.txt": "content of file 2",
        "/home/mocked-folder/file3.txt": "yet another content",
        "/home/mocked-folder/file4.txt": "one more content",
    }


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
