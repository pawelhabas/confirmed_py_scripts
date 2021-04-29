#   Projects Review
__version__ = "0.1.0"

import pathlib

"""
This is script to get informations about whole directory of scripts.
It can walk trough the folders and files looking for:
 1. files named readme.txt
 2. other files with comment in the begining like this one
It should give posibility of adding readme.txt files in specific directory
"""

"""
STEPS:
1. read and print names of all folders in "D:/" directory with word "DIR" in begining
2. read and print names of all files in "D:/" directory
"""




# __version__ = "0.1.0"
# root_dir = pathlib.Path(my_root_dir)
# print(root_dir)
# entries = root_dir.iterdir()
# print(entries)
# entries = sorted(entries, key=lambda entry: entry.is_file())
# entries_count = len(entries)
# for index, entry in enumerate(entries):
#     if entry.is_dir():
#         print('DIR ',entry)
#     else:
#         print(entry)

__version__ = "0.1.1"

import os

my_root_dir = f'D:\py_git'
szukane = 'datatime'
# import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

def szukaj(adres):
    # print(adres)
    tekst = open(adres,encoding='utf-8').read()
    tekst.replace('.',' ')
    tab = tekst.lower().split(' ')
    #print(tab)
    #raise Exception
    if 'datetime' in tab:
        print(adres)
    pass

class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            if szukane != '':
                print(entry)


class _TreeGenerator:
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                if entry.name[0] != '.' and entry.name != 'venv':
                    self._add_directory(
                        entry, index, entries_count, prefix, connector
                    )

            else:
                if szukane != '':
                    if entry.name[-3:] == '.py':
                        szukaj(f"{entry}")
                self._add_file(entry, prefix, connector)

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(
            directory=directory,
            prefix=prefix,
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")


tree = DirectoryTree(my_root_dir)  # my_root_dir
tree.generate()

