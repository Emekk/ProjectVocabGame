import csv
import json
from typing import Dict


PATH_VOCAB_CSV = "csv original/vocab.csv"
PATH_PIP_CSV = "csv original/pip.csv"
ENCODING = "utf-8-sig"
PATH_VOCAB_JSON = "json original/vocab.json"
PATH_PIP_JSON = "json original/pip.json"

def vocab_word_dict(vocab_csv_path, encoding) -> Dict[str, list]:
    with open(vocab_csv_path, encoding=encoding) as f:
        reader = csv.reader(f)
        keys = {key.lower():i for i, key in enumerate(next(reader))}
        word_dict = {}
        for row in reader:
            word_dict[row[keys["word"]]] = []  # add each word as a key to 'word dict'
            # clean 'meaning'
            meaning = row[keys["meaning"]].split('/')
            word_dict[row[keys["word"]]].append(meaning)
            # clean 'pos'
            pos = row[keys["pos"]].split(',')
            word_dict[row[keys["word"]]].append(pos)
            # clean 'collocation'
            colloc = row[keys["collocation"]]
            if colloc == 'NaN':
                word_dict[row[keys["word"]]].append(None)
            else:
                colloc = colloc.split('/')
                word_dict[row[keys["word"]]].append(colloc)
            # clean 'notes'
            notes = row[keys["notes"]]
            if notes == 'NaN':
                word_dict[row[keys["word"]]].append(None)
            else:
                word_dict[row[keys["word"]]].append(notes)
            # clean 'date'
            date = row[keys["date"]].split("-")
            date = "/".join(reversed(date))
            word_dict[row[keys["word"]]].append(date)
        return word_dict

def pip_phrase_dict(pip_csv_path, encoding) -> Dict[str, list]:
    with open(pip_csv_path, encoding=encoding) as f:
        reader = csv.reader(f)
        keys = {key.lower():i for i, key in enumerate(next(reader))}
        pip_dict = {}
        for row in reader:
            pip_dict[row[keys["pip"]]] = []  # add each word as a key to 'word dict'
            # clean 'meaning'
            meaning = row[keys["meaning"]].split('/')
            pip_dict[row[keys["pip"]]].append(meaning)
            # clean 'date'
            date = row[keys["date"]].split("-")
            date = "/".join(reversed(date))
            pip_dict[row[keys["pip"]]].append(date)
        return pip_dict

def main() -> None:
    # transform & save vocab.csv as vocab.json
    vocab_dict = vocab_word_dict(PATH_VOCAB_CSV, ENCODING)
    with open(PATH_VOCAB_JSON, 'w') as f:
        json.dump(vocab_dict, f)

    # transform & save vocab.csv as vocab.json
    pip_dict = pip_phrase_dict(PATH_PIP_CSV, ENCODING)
    with open(PATH_PIP_JSON, 'w') as f:
        json.dump(pip_dict, f)


if __name__ == "__main__":
    main()
