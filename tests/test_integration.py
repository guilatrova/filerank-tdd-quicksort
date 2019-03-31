import os

from main import read_files


def test_integration_read_files():
    """
    Uses integration test to make sure we're expecting the correct output.
    For such test we should stick to simplicity in order to
    be resilient to changes.
    """
    cur_path = os.path.dirname(os.path.realpath(__file__))
    result = read_files(cur_path)

    thisfilepath = f"{cur_path}/test_integration.py"
    thistestmethod = "test_integration_read_files"

    assert thisfilepath in result
    assert thistestmethod in result[thisfilepath]
