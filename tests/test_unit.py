import pytest

from main import trim_search_words


@pytest.fixture()
def mocked_files(mocker):
    files = {
        "/home/mocked-folder/file1.txt": "content of file 1",
        "/home/mocked-folder/file2.txt": "content of file 2",
        "/home/mocked-folder/file3.txt": "yet another content",
    }

    mocker.patch("main.read_files", return_value=files)


def test_trim_search_words_outputs_set():
    trimmed = trim_search_words(["to", "be", "or", "not", "to", "be"])

    assert len(trimmed) == 4
    assert isinstance(trimmed, set)
