from os import listdir
from os.path import isfile


def read_files(path):
    filenames = listdir(path)
    contents = {}
    for filename in filenames:
        fullpath = f"{path}/{filename}"
        if isfile(fullpath):
            with open(fullpath, "r") as content:
                contents[fullpath] = content.read().replace("\n", "")

    return contents


def trim_search_words(words):
    return set(words)


def rank_files(words, files):
    results = {}
    for file in files:
        results[file] = 100

    return results


if __name__ == "__main__":
    pass
