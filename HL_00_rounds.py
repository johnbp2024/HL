def int_check(question):
    while True:
        error = "please enter a integer that is 1 or more"

        to_check = input(question)
        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

print("⬆️⬆️⬆️welcome to higher or lower game⬇️⬇️⬇️")
print()

want_instructions = yes_no("do you want to see the instructions? ").lower()
if want_instructions == "yes":
    instructions()
print()
print("program continues")

# ask for number of rounds/infinite mode
num_rounds = int_check("how many rounds would you like? or press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# game loop starts here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if players are in inf mode then increase the rounds
    if mode == "infinite":
        num_rounds += 1
