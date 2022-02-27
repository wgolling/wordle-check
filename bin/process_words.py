from pathlib import Path 
from datetime import datetime
import json
import hmac

def process_words(raw_answers_path, processed_words_path):
    words_by_date = dict()
    with open(raw_answers_path) as file:
        file.readline()                                                       # First line is just headings.
        line = file.readline()
        while line:
            date_string,_,word = _process_line(line)
            words_by_date[date_string] = word
            line = file.readline()
    # with open(processed_words_path, 'w') as file:
    #     json.dump(words_by_date, file)
    encrypted_dict = _digest_words_dict(words_by_date)
    print(encrypted_dict)
    with open(processed_words_path, 'wb') as file:
        file.write(encrypted_dict)
    

def _process_line(line):
    '''
    Assumes line is of the form f'mm/dd/yyyy\t{game_number}\t{word}'
    Returns strings representing the date,
                                 the game,
                                 the word.
    '''
    line_parts = line.split('\t')
    date_string = datetime.strptime(line_parts[0], '%m/%d/%Y').isoformat()    # Convert datestring to ISO format.
    game_number = line_parts[1]
    word = line_parts[2].strip()
    return date_string,game_number,word

def _digest_words_dict(words_dict):
    '''
    Returns the json representation of words_dict, encrypted into bytes with MD5.
    '''
    json_string = json.dumps(words_dict).encode()
    digester = hmac.new("Dummy key, doesn't matter".encode())
    digester.update(json_string)
    return digester.digest()



if __name__ == "__main__":
    raw_answers_path        = Path('.') / 'data' / 'raw_answers.txt'
    processed_words_path    = Path('.') / 'data' / 'processed_words.py'
    process_words(raw_answers_path, processed_words_path)
