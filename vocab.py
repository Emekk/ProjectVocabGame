import json
from typing import List
from word import Word


PATH_VOCAB_DATA = "data/json original/vocab.json"


def load_word_json(vocab_json_path: str) -> List[Word]:
    """Loads 'Word's in a JSON file to a list and returns it."""
    word_list = []
    with open(vocab_json_path) as f:
        word_dict = json.load(f)
        for key in word_dict:
            w = Word(key, *word_dict[key])
            word_list.append(w)
    return word_list


class Vocab:
    """Class for storing and managing 'Word's"""
    def __init__(self, word_list: List[Word] = None):
        if word_list is None:
            self.__word_list = load_word_json(PATH_VOCAB_DATA)
        else:
            self.__word_list = word_list

    @property
    def word_list(self):
        return self.__word_list
