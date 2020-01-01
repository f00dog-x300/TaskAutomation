import os


CONTENT = "content"

def test_create_file(tmp_path):

    # created test directory
    test_dir = tmp_path / "source"
    test_dir.mkdir()
    # creating the test file inside test directory
    test_file = test_dir / "test_file.txt"
    test_file.write_text(CONTENT)
    assert test_file.read_text() == CONTENT

