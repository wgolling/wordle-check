from pathlib import Path 
from datetime import datetime
import json

def process_words(raw_answers_path):
    words_by_date = dict()
    with open(raw_answers_path) as file:
        file.readline() # First line is just headings
        line = file.readline()
        while line:
            date_string,game_number,word = _process_line(line)
            words_by_date[date_string] = word
            line = file.readline()
    processed_words_path = Path('.') / 'data' / 'processed_words.py'
    with open(processed_words_path, 'w') as file:
        json.dump(words_by_date, file, default=str)

def _process_line(line):
    '''
    line is of the form 'mm/dd/yyyy\t{game_number}\t{word}'
    returns the date as a datetime.date object,
            the game number as an integer,
            the word as a string
    '''
    line_parts = line.split('\t')
    date_string = datetime.strptime(line_parts[0], '%m/%d/%Y').isoformat()
    game_number = int(line_parts[1])
    word = line_parts[2].strip()
    return date_string,game_number,word

if __name__ == "__main__":
    raw_answers_path = Path('.') / 'data' / 'raw_answers.txt'
    process_words(raw_answers_path)
