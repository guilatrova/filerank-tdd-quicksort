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


def _calculate_rank_result(words, content):
    """
    Receives expected words to look for and calculates a proper rank
    based on how many words are actually found
    """
    found = 0
    for word in words:
        if word in content:
            found += 1

    return _calculate_result(found, len(words))


def _calculate_result(found, total):
    """ Calculates real result based on found words vs total words """
    return (found * 100) / total


def rank_files(words, files):
    results = {}
    for filename in files:
        results[filename] = _calculate_rank_result(words, files[filename])

    return results


if __name__ == "__main__":
    pass
