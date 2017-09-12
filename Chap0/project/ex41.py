import random # import random module
from urllib.request import urlopen #change urllib in the book to urllib.request, diffrence in python3
import sys #import module

WORD_URL = "http://learncodethehardway.org/words.txt" #uniform resourse location
WORDS = [] #a list

PHRASES = { #a dict
  "class %%%(%%%)":
    "Make a class named %%% that is-a %%%.",#a key and value,likes a class and interpretation,is-a inheritance,the class inherited another class
  "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has_a __init__  that takes self and *** parameters.",#a key and value, likes a class ,in the class, there is a instantiated function,self and *** are parameters
  "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ paramrters.",#a key and a value,likes a class,there is a function in the class,
  "*** = %%%()":
    "Set *** to an instance of class %%%.",# a key and its value,likes givng the value of the class to a variable ***
  "***.***(@@@)":
    "From *** get the *** function, and call it with paeameters self, @@@.",#a key and its value, likes from a class get a function and calls two parameters
  "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."# a keyand its value,from a class get an attribute and sets to a variable
}

#do they want to drill phrases first
PHRASE_FIRST = False # set the variable to a value
if len(sys.argv) == 2 and sys.argv[1] == "english": #if sentence,the length of argument variable eauals to 2 and the second argv is "english"
    PHRASE_FIRST == True #then the variable is True

 #load up the words from the website
for word in urlopen(WORD_URL).readlines():       # a loop,urlopen() gets information from the website of the url, readlines() reads the information,word circles the information
    WORDS.append(word.strip())    #strip() moves away a certain string,usally space move away space in the list word,appends to list WORD


def convert(snippet, phrase):       #a function convert, two parameters
    class_name = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))] #list class_name,capitalize() puts the first letter upper case, random.sample(sequence, k) gets k elements in sequence at random

    other_names = random.sample(WORDS, snippet.count("***"))#random.sample(sequence,k) gets k elements from WORDS at random
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3) #get a number in the range at random
        param_names.append(','.join(random.sample(WORDS, param_count))) #join() combines the words without comma ,add them to the list param_names

        for sentence in snippet, phrase:  # lists
            result = sentence[:] #copy the list

            #fake class names
        for word in class_name:
            result = result.replace("%%%", word, 1) #replace(),use list word replace the 1st "%%%"

            #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

            #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


#keep going until they hit CTRL_D
try:                    #debug
    while True:
        snippets = PHRASE.keys()          #object.keys() returns all the keys of a dict in a list
        random.shuffle(snippets) #gets a mixed order

        for snippet in snippets:
            phrase = PHRASE[snippet]
            question, answer = convert(snippet, phrase) #call the function
            if PHRASE_FIRST:
                question, answer = answer, question

            print (question)

            input(">")
            print ("ANSWER: %s\n\n" % answer)
except EOFError:
    print ("\nBye")
