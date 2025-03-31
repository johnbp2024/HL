def yes_no(question):
    """checks user response to question is yes or no/y or n then returns yes or no then"""
    while True:
        response = input(question).lower()
        #  #user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


def instructions():
    """prints instructions"""
    print("""
***instructions***

to start, chose the number of rounds then ether 
customise the game peramitors or go with the defalt game 
(the number between 1 and 100)

then choose how many rounds to play or press enter for infinite mode 

try to guess the number without running out of guesses 

good luck  
    """)


# main routine goes here
print()
print("⬆️⬆️⬆️welcome to the higher or lower game⬇️⬇️⬇️")

want_instructions = yes_no("do you want to see the instructions? ").lower()
if want_instructions == "yes":
    instructions()
print()
print("program continues")
