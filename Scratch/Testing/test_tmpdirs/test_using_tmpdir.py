# reference is from Brian Okken's book
# using tmpdir_factory for session scope on a test
def test_tmpdir(tmpdir):
    # tmpdir already has a path name associated with it
    # join() extends the path to include a filename
    # the file is creaed when its written to
    a_file = tmpdir.join('something.txt')

    # creation of subdirectories
    a_sub_dir = tmpdir.mkdir('anything')

    # you can create files in directories (remember, created when written only)
    aanother_file_sub = a_sub_dir.join('something_else.txt')