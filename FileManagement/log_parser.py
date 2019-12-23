import codecs
import pathlib

bad_path = pathlib.Path(
    r"..\ExampleFiles\170001451SW_Pulled_12052019_143006_PST.log")
good_path = pathlib.Path(
    r"..\ExampleFiles\[Com COM26] (2019-12-20_133052).log")


def log_reader(filepath):
    with codecs.open(filepath, encoding="utf-8-sig") as readfile:
        contents = readfile.read()
        yield contents


for line in log_reader(bad_path):
    try:
        print(line)
    except UnicodeEncodeError:
        line = line.encode("utf8")
        print(line)
