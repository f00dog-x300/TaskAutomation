


CONTENT = "content"

def test_create_file(tmp_path):
    """Testing how to move one file"""
    # creating test directories
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "destination"
    source_dir.mkdir()
    destination_dir.mkdir()

    # calling instance of FileMover
    filemover = FileMover(source_dir, destination_dir)

    # creating the test file inside test directory
    test_file = source_dir / "test_file.txt"
    test_file.write_text(CONTENT)

    # testing moving file to the destination 
    filemover(test_file, destination_dir)
    file_dest_dir_state = destination_dir / "test_file.txt"

    # TODO : Assert that the temporary file is in the destination folder

