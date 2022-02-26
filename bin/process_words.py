from pathlib import Path 
from datetime import date

def process_words(raw_answers_path):
    with open(raw_answers_path) as file:
        file.readline() # First line is just headings
        line = file.readline()
        steps = 0
        while line and steps < 200:
            line_parts = line.split('\t')
            date_parts = list(map(int, line_parts[0].split("/")))
            date_obj = date(date_parts[2],date_parts[0],date_parts[1])
            game_number = int(line_parts[1])
            word = line_parts[2].strip()
            print(date_obj)
            print(game_number)
            print(word)
            line = file.readline()
            steps += 1

if __name__ == "__main__":
    raw_answers_path = Path('.') / 'data' / 'raw_answers.txt'
    process_words(raw_answers_path)
