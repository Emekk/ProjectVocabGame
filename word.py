from dataclasses import dataclass
from typing import Union, Set


@dataclass
class Word:
    """Class for keeping properties of a word that constitutes a Vocabulary."""
    word: str
    meaning: Set[str]
    pos: Set[str]
    collocation: Union[None, str, Set[str]]
    notes: Union[None, str]
    date: str
