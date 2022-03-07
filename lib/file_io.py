'''
Handles file operations.

One of the main purposes of this module is to encapsulate file paths.
'''

from pathlib import Path
import json

_RAW_WORDS_PATH         = Path('.') / 'data' / 'raw_answers.txt'
_PROCESSED_WORDS_PATH   = Path('.') / 'data' / 'processed_words.txt'
_INVERTED_WORDS_PATH    = Path('.') / 'data' / 'inverted_words.txt'

class RawWords():
    '''
    Basic context manager that loads the raw words file.
    '''

    def __init__(self):
        self.file_obj = open(_RAW_WORDS_PATH)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def save_words_dict(words_dict):
    _save_to_file(words_dict, _PROCESSED_WORDS_PATH)

def save_dates_by_words_dict(dates_by_words):
    _save_to_file(dates_by_words, _INVERTED_WORDS_PATH)

def _save_to_file(dict_, filepath):
    with open(filepath, 'w') as file:
        json.dump(dict_, file)

def load_inverted_words():
    with open(_INVERTED_WORDS_PATH) as file:
        d = json.load(file)
    return d
