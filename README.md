# Wordle Check

Lets you check [Wordle](https://www.nytimes.com/games/wordle/index.html) guesses against a collection of previous answers. It will not use information about the current day or future days, only answers that have previously happened.

Disclaimer: this project is based on a list of answers before the New York Times acquired the game. NYT answers after that point may give a false negative and original answers may give a false positive. It's just for fun.

The answer collection came from a reddit thread I can't find anymore. There are more up-to-date answer lists out there now so the project should be updated as well. 

Much of the repo consists of scripts for processing the raw answers into amenable data structures and then saving them in an encrypted format. The file `data/letter_stats.txt` has statistics about letter frequencies. 


## Getting started

A windows executable (built in Windows 10, x64) called `wordle_check.exe` is in the `deploy/dist` folder. In other operating systems you will have to run `python3 main.py`.

## Usage

```
<path_to_exe>\wordle_check.exe <guess>
```
where `<guess>` is a 5-character alphabetic string. If `<guess>` is found in the answer collection prior to the current date then the program will return the date it was the answer in the original game, otherwise it prints "Word unused".
