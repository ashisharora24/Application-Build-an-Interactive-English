# only for testing
import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    return "The word {} doesnot exist. Please double check it.".format(word)


word = input("Enter the word : ")
print(translate(word))
