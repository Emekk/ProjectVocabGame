import json
from typing import List
from phrase import Phrase


PATH_PIP_DATA = "data/json original/pip.json"


def load_phrase_json(pip_json_path: str) -> List[Phrase]:
    """Loads 'Phrase's in a JSON file to a list and returns it."""
    phrase_list = []
    with open(pip_json_path) as f:
        word_dict = json.load(f)
        for key in word_dict:
            p = Phrase(key, *word_dict[key])
            phrase_list.append(p)
    return phrase_list


class PIP:
    """Class for storing and managing 'Phrase's"""
    def __init__(self, phrase_list: List[Phrase] = None):
        if phrase_list is None:
            self.__phrase_list = load_phrase_json(PATH_PIP_DATA)
        else:
            self.__phrase_list = phrase_list

    @property
    def phrase_list(self):
        return self.__phrase_list
