import pytest

from main import read_files


@pytest.fixture()
def files():
    return {
        "/home/mocked-folder/file1.txt": "content of file 1",
        "/home/mocked-folder/file2.txt": "content of file 2",
        "/home/mocked-folder/file3.txt": "content of yet another file",
    }


def test_read_files(files):
    filesread = read_files("/home/mocked-folder")

    assert len(filesread) == 3
    for fileread in filesread:
        assert fileread.startswith("/home/mocked-folder")
