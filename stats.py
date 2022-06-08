import lib.file_io as file_io
from collections import defaultdict
from string import ascii_lowercase

# Initialize and filter words dict.
data = file_io.load_inverted_words()
max_date = "2027-10-21"
data = dict(filter(lambda elem: elem[1] < max_date, data.items()))

# Initialize stats dict.
int_dict_factory = lambda: defaultdict(int)
stats = defaultdict(int_dict_factory)

# Populate stats dict.
for word in data.keys():
    freq = defaultdict(int)
    for char in word:
        freq[char.lower()] += 1
    for char in freq:
        c = char.lower()
        stats[c][freq[c]] += 1

# Compute occurrence percentages and write to a string.
stats_string = ""
word_count = len(data)
for c in ascii_lowercase:
    char_stats = stats[c]
    char_stat_strings = []
    for i in range(len(char_stats)):
        stat = char_stats[i+1]
        percent = float(stat) / word_count 
        percent_string = f"{percent : .2%}"
        if (stat * 100) // word_count < 10:
            percent_string = " " + percent_string
        char_stat_strings.append(percent_string)
    char_string = f"{c}:"
    for p in char_stat_strings:
        char_string = char_string + "   " + p    
    stats_string += char_string + "\n"

# Save stats string.
stats_file_path = file_io._LETTER_STATS
with open(stats_file_path, 'w') as f:
    f.write(stats_string)
