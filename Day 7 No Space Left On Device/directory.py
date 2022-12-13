import file
from typing import List


class directory:
    def __init__(
        self, name, parent, dirlist: list, filelist: List[file.file]
    ) -> None:
        self.name = name
        self.parent = parent
        self.dirlist = dirlist
        self.filelist = filelist

    def set_name(self, name: str):
        self.name = name

    def set_parent(self, parent):
        self.parent = parent

    def add_dir(self, dir):
        self.dirlist.append(dir)

    def rm_dir(self, dir):
        self.dirlist.remove(dir)

    def add_file(self, file: file):
        self.filelist.append(file)

    def rm_file(self, file: file):
        self.filelist.remove(file)

    def get_size(self) -> int:
        size = 0
        for dir in self.dirlist:
            size += dir.get_size()
        for file in self.filelist:
            size += file.size
        return size

    def get_all_subdirs(self) -> list:
        subdirs = []
        for dir in self.dirlist:
            subdirs.append(dir)
            subdirs += dir.get_all_subdirs()
        return subdirs
