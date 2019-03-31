from os import listdir
from os.path import isfile


def _read_file_content(filename):
    with open(filename, "r") as content:
        return content.read().replace("\n", "")


def read_files(path):
    """
    Reads all files inside a given directory path, then
    filters folders and returns a dict where key is the filename
    and value is the actual contents
    """
    filenames = listdir(path)
    contents = {}
    for filename in filenames:
        fullpath = f"{path}/{filename}"
        if isfile(fullpath):
            contents[fullpath] = _read_file_content(fullpath)

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
        # NOTE: We could use regex, but since we might avoid libs
        # we're going to filter stuff ourselves
        begin_word = f"{word} "
        end_word = f" {word}"
        middle_word = f" {word} "

        if word == content:
            found += 1
        elif middle_word in content:
            found += 1
        elif content.startswith(begin_word) or content.endswith(end_word):
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


def process_input(rawinput):
    return rawinput.split()


def generate_output(filename, value):
    stripfrom = filename.rfind("/") + 1
    onlyname = filename[stripfrom:]
    return f"{onlyname} - {value:.2f}%"


if __name__ == "__main__":
    pass
