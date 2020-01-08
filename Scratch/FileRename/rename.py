from pathlib import Path 


p_folder = "/home/f00dog/Documents/Dev/TaskAutomation/Scratch/FileRename/"
p_txt = "/home/f00dog/Documents/Dev/TaskAutomation/Scratch/FileRename/"
p_other = "/home/f00dog/Documents/Dev/TaskAutomation/Scratch/FileRename/other_orig.log"

# Path(p_folder).rename('/home/f00dog/Documents/Dev/TaskAutomation/Scratch/FileRename/Blah')
# Path(p_txt, "original.txt").rename(Path(p_txt, "blah.txt"))

class FileRename:

    def rename(self, src, trgt):
        """Renames the file"""
        renamed = Path(src)
        renamed.rename(trgt)


rename = FileRename()
original = Path(p_folder, "original")
target = Path(p_folder, "changed")
rename.rename(original, target)
