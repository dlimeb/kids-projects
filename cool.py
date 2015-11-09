import random
import re

# ask for an acronym
acronym = ""
while not acronym:
    acronym = raw_input("Type in an acronym to use: ")

letters = list(acronym.lower())

# put the dictionary into a list
dict_file = open("/usr/share/dict/words", "r")
dictionary = []

for line in dict_file:
    dictionary.append(line.rstrip("\n"))

insult = []

# for each letter, find all the dictionary words that start with that letter, and pick one at random
for l in letters:
    choices = []
    for word in dictionary:
        if re.match("^%s" % l, word):
            choices.append(word)

    word = random.choice(choices)
    insult.append(word)

print "Oh yeah? Well you are a " + " ".join(insult) + "!"
