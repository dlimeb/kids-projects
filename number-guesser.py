import random

your_name = ""

while not your_name:
    your_name = raw_input("Hello there! Type in your name: ")

print "Hi " + your_name + "! Let's play a game, ok?"
print "I'm thinking of a number between 1 and 10. Try to guess it! You have 5 tries."

the_number = random.randint(1,10)
answer_is_wrong = True
number_of_guesses = 0
guesses_so_far = []

while number_of_guesses < 5:
    the_guess = raw_input("Your number: ")

    if not the_guess:
        print "Hey! You forgot to type something!"
        continue

    number_of_guesses += 1

    try:
        the_guess = int(the_guess)
    except:
        print "That wasn't a number!"
        continue

    if the_guess < 1:
        print "That number was too low."
        continue

    if the_guess > 10:
        print "That number was too high."
        continue

    if the_guess == the_number:
        answer_is_wrong = False
        print
        print "YOU WIN!"
        if number_of_guesses is 1:
            print "Holy moly, you got it in one guess!"
        else:
            print "You got it in %s guesses!" % number_of_guesses 
        break
    else:
        if the_guess in guesses_so_far:
            print "Oh my chick peas! You guessed that already!!"
        else:
            print "Sorry, that wasn't it. You have %s left!" % (5 - number_of_guesses)

        guesses_so_far.append(the_guess)

if answer_is_wrong:
    print
    print "I win! You couldn't guess the number! It was %s." % the_number

print "Bye bye."
