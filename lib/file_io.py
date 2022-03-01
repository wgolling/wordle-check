'''
Handles file operations.

One of the main purposes of this module is to encapsulate file paths.
'''

from pathlib import Path
import json

_RAW_WORDS_PATH         = Path('.') / 'data' / 'raw_answers.txt'
_PROCESSED_WORDS_PATH   = Path('.') / 'data' / 'processed_words.txt'

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
    with open(_PROCESSED_WORDS_PATH, 'w') as file:
        json.dump(words_dict, file)
