'''
Handles file operations.
'''

from pathlib import Path
import json

_RAW_WORDS_PATH         = Path('.') / 'data' / 'raw_answers.txt'
_PROCESSED_WORDS_PATH   = Path('.') / 'data' / 'processed_words.txt'

class RawWords():

    def __init__(self):
        self.file_obj = open(_RAW_WORDS_PATH)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def save_words_dict(words_dict):
    with open(_PROCESSED_WORDS_PATH, 'w') as file:
        json.dump(words_dict, file)
