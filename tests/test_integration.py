import os

from main import read_files


def test_integration_list_files():
    """
    Uses integration test to make sure we're expecting the correct output.
    For such test we should stick to simplicity in order to
    be resilient to changes.
    """
    cur_path = os.path.dirname(os.path.realpath(__file__))
    result = read_files(cur_path)

    assert f"{cur_path}/test_integration.py" in result
    assert "test_integration_list_files" in result["test_integration.py"]
