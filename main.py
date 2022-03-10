import sys
from datetime import date
from lib.file_io import load_inverted_words

def _print_hello():
    print("hello")

def _query(word):
    words_dict = load_inverted_words()
    if word not in words_dict:
        return "Word unused"
    word_date = date.fromisoformat(words_dict[word])
    today = date.today()
    return word_date if word_date < today else "Word unused"

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        _print_hello()
    else:
        word = str(args[0])
        q = _query(word)
        print(q)
