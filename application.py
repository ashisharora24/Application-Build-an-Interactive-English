# only for testing
import json

data = json.load(open("data.json"))

def translate(word):
    return data[word]

word = input("Enter the word : ")
print(translate(word))
