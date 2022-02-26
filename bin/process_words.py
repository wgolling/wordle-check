from pathlib import Path 
from datetime import datetime

def process_words(raw_answers_path):
    with open(raw_answers_path) as file:
        file.readline() # First line is just headings
        line = file.readline()
        while line:
            date_obj,game_number,word = _process_line(line)
            print(date_obj)
            print(game_number)
            line = file.readline()

def _process_line(line):
    '''
    line is of the form 'mm/dd/yyyy\t{game_number}\t{word}'
    returns the date as a datetime.date object,
            the game number as an integer,
            the word as a string
    '''
    line_parts = line.split('\t')
    date_obj = datetime.strptime(line_parts[0], '%m/%d/%Y')
    game_number = int(line_parts[1])
    word = line_parts[2].strip()
    return date_obj,game_number,word

if __name__ == "__main__":
    raw_answers_path = Path('.') / 'data' / 'raw_answers.txt'
    process_words(raw_answers_path)
