import os
import sys


def project_directory() -> str:
    return os.path.commonpath([i for i in sys.path if os.getcwd().split(":")[0] == i.split(":")[0]])


def walker(filepath: str):
    tmp: list = []
    try:
        for root, dirs, files in os.walk(filepath):
            for file in files:
                tmp.append(dict(filename=file, filepath=os.path.join(root, file)))
        return tmp
    except FileExistsError:
        print('FileExistsError: Walk path does not exist, please try again.')
