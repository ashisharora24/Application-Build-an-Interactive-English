# only for testing
import json

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    return "The word {} doesnot exist. Please double check it.".format(word)


word = input("Enter the word : ")
print(translate(word))
