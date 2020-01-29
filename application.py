# only for testing
import json

# importing diff for handling the best matching solutions
import difflib
from difflib import get_close_matches

# importing json file
data = json.load(open("data.json"))

def translate(word):
    '''
        1. method to take the import as word
            and return its meaning
        2. if word doesnot exist then it will suggest closest similar words
        3. if no closest similar word exist, then it will pass returning
            statement that word doesnt exist
    '''
    w = word.lower()
    if w in data:
        return data[w]

    # incase word doesn't exist
    # get the list of close words
    close_match_list = get_close_matches(w,data.keys())
    if len(close_match_list)>0:
        # if the close words exist, then we will suggest them
        print('We didnt find your word in dictionary, but we found some close match')
        print("Press appropriate number or press 0 to exist")
        count = 1
        for i in close_match_list:
            print("Press {} : {}".format(count,i))
            count+=1

        select_condition = True
        while select_condition:
            selection = int(input("Enter your selection or press 0 to exist : "))
            if selection==0:
                return "Thank You for your time"
            elif 0<selection<count:
                select_condition = False
                print(close_match_list[selection-1])
                return translate(close_match_list[selection-1])
            else:
                print("You have entered incorrect select. please try again")

    # incase get_close_words doesnt exist, then we will return the statement
    return "The word {} doesnot exist. Please double check it.".format(word)

word = input("Enter the word : ")
print(translate(word))
