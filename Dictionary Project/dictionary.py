import json
from difflib import get_close_matches

data = json.load(open("Data/dictionary_data.json"))
print("Welcome to my Dictionary...")
print("#------------------------------------------------------------------------------------------------------#")

def meaning(word):
    word= word.lower() #convert word in small letter
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()] #convert the word in capital letter
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("press y for yes and n for no. ")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return ("Your spell is incorrect please enter vaild spell")
        else:
            return("Opps your input is wrong...!!!")
    else:
        print("Your spell is incorrect please enter vaild spell.")


word=input("Enter spell you want to know there meaning : ")

mean= meaning(word)


if type(mean)==list: #if word have more than one meaning
    for item in mean:
        print(item)
else:
    print(mean)