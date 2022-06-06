from dataclasses import dataclass
from typing import Set

@dataclass
class Phrase:
    """Class for keeping properties of a phrase that constitutes a PIP."""
    phrase: str
    meaning: Set[str]
    date: str
