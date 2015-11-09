print "Hi there! Let's play Name Scrambler!"

your_name = ""
while not your_name:
    your_name = raw_input("Type in your name: ")

print "OK", your_name

print "Choose a way to scramble your name:"
print "  1. Make it uppercase."
print "  2. Make it backwards."
print "  3. Make it tall."

your_choice = ""
while not your_choice:
    your_choice = raw_input("Enter your choice: ")

if your_choice is "1":
    print "Your name scrambled is:", your_name.upper()
if your_choice is "2":
    print "Your name scrambled is:", your_name[::-1]
if your_choice is "3":
    print "Your name scrambled is:",
    for l in your_name:
        print l + " "

print "That's it. Bye bye!"
