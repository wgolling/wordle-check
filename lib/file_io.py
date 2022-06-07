'''
Handles file operations.

The main purposes of this module are to encapsulate file paths, and
handle encryption of the word dictionaries.
'''

from pathlib import Path
import json
from cryptography.fernet import Fernet

_RAW_WORDS_PATH         = Path('.') / 'data' / 'raw_answers.txt'
_PROCESSED_WORDS_PATH   = Path('.') / 'data' / 'processed_words.txt'
_INVERTED_WORDS_PATH    = Path('.') / 'data' / 'inverted_words.txt'
_LETTER_STATS           = Path('.') / 'data' / 'letter_stats.txt'
_CRYPT_PATH             = Path('.') / 'lib'  / 'crypt.key'

class Crypto():
    '''
    Handles encryption and decryption of strings.
    '''

    def __init__(self):
        with open(_CRYPT_PATH, "rb") as file:
            key = file.read()
        self.fernet = Fernet(key)

    def string_to_encrypted_bytes(self, string):
        return self.fernet.encrypt(string.encode())

    def encrypted_bytes_to_string(self, bytes):
        return self.fernet.decrypt(bytes).decode()

# Saving.

def save_words_dict(words_dict):
    _save_to_file(words_dict, _PROCESSED_WORDS_PATH)

def save_dates_by_words_dict(dates_by_words):
    _save_to_file(dates_by_words, _INVERTED_WORDS_PATH)

def _save_to_file(dict_, filepath):
    dict_string = json.dumps(dict_)
    encoded = Crypto().string_to_encrypted_bytes(dict_string)
    with open(filepath, 'wb') as file:
        file.write(encoded)

# Loading.

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

def load_inverted_words():
    with open(_INVERTED_WORDS_PATH, 'rb') as file:
        bytes = file.read()
    return json.loads(Crypto().encrypted_bytes_to_string(bytes))
