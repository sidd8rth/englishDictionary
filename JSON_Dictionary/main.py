import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input(f"Did you mean {get_close_matches(word,data.keys(), cutoff=0.8)[0]} instead? Enter Y if yes or N for no : ").upper()
        if yn == 'Y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == 'N':
            return "Sorry, The word you are trying to find meaning of, doesn't exist'"
        else:
            return "Sorry, Can't understand your query"
    else:
        return "This word doesn't exist, Please double check you input and try again"


while True:
    w = input("Enter Word you want to search , or to exit enter Q : ")
    if w == 'q' or w == 'Q':
        exit()
    output = translate(w)
    if isinstance(output, list):
        print('Meaning is as follows : ')
        for i in range(len(output)):
            print(f"{i+1} : {output[i]}")
    else:
        print(output)
    print()
