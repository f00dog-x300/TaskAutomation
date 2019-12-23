from pathlib import Path
import shutil


class FileMover:

    def __init__(self, src, dest):
        self.source = src
        self. destination = dest

    def file_mover(self):
        shutil.move(str(self.source), str(self.destination))

    def filetype_check(self, suffix_type):
        for file in Path.iterdir(self.source):
            if Path.is_file(file) is True:
                if Path(file).suffix == suffix_type:
                    self.file_mover()


if __name__ == "__main__":
    filemover = FileMover(src=Path(r"C:\Users\klao\Documents\Personal\taskautomation\source"),
                          dest=Path(r"C:\Users\klao\Documents\Personal\taskautomation\tmp"))
    filemover.filetype_check(".txt")
