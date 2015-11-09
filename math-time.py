import random

print
name = ""
while not name:
    name = raw_input("Hello there. What is your name? ")
print
print "OK %s, it's math time!" % name
print

keep_going = True

while keep_going:
    number_one = random.randint(0,20)
    number_two = random.randint(0,20)

    operator = ""
    while not operator:
        operator = raw_input("Do you want to add or subtract? +/- ")
        if not(operator is "+" or operator is "-"):
            print "Oops! You didn't enter a '+' or a '-'"
            operator = ""
        print

    if number_two > number_one:
        tmp_number = number_two
        number_two = number_one
        number_one = tmp_number

    guess = ""
    while not guess:
        guess = raw_input("What is %s %s %s? " % (number_one, operator, number_two))

    print "You guessed: %s" % guess

    if operator == "+":
        answer = number_one + number_two
    else:
        answer = number_one - number_two

    if answer == int(guess):
        print "HOORAY, YOU GOT IT RIGHT!!!"
    else:
        print "Sorry, you got it wrong :( This was the answer: %s" % answer

    print
    prompt = raw_input("Enter 'q' to quit, or any other letter to keep going! ")
    print

    keep_going = prompt != "q"

print "See you later!"
