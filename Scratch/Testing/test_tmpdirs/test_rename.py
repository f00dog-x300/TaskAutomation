# reference is from https://docs.pytest.org/en/latest/tmpdir.html
CONTENT = "content"

def test_create_file(tmpdir):
    d = tmpdir / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding=None)

    print("here: ", d)
    assert p.read_text(encoding=None) == "content"
    assert len(list(tmpdir.listdir())) == 1


## notes
"""
 using tmpdir vs tmp_path
 - tmpdir acts more like py.path where tmp_path acts more like pathlib
    - reference for py.path
        - https://py.readthedocs.io/en/latest/path.html

"""