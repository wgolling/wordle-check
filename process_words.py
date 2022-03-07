from datetime import datetime
from lib.file_io import RawWords, save_words_dict, save_dates_by_words_dict

def process_words():
    words_by_date = dict()
    with RawWords() as file:
        file.readline()                                                       # First line is just headings.
        line = file.readline()
        while line:
            date_string,_,word = _process_line(line)
            words_by_date[date_string] = word
            line = file.readline()
    save_words_dict(words_by_date)
    dates_by_words = _invert_dict(words_by_date)
    save_dates_by_words_dict(dates_by_words)

def _process_line(line):
    '''
    Assumes line is of the form f'mm/dd/yyyy\t{game_number}\t{word}'
    Returns strings representing the date, in ISO format,
                                 the game number,
                                 the word.
    '''
    line_parts = line.split('\t')
    date_string = datetime  .strptime(line_parts[0], '%m/%d/%Y')    \
                            .date()                                 \
                            .isoformat()                                      # Convert datestring to ISO format.
    game_number = line_parts[1]
    word = line_parts[2].strip()
    return date_string,game_number,word

def _invert_dict(words_by_date):
    dates_by_words = dict() 
    for date_string, word in words_by_date.items():
        dates_by_words[word] = date_string
    return dates_by_words

if __name__ == "__main__":
    process_words()
