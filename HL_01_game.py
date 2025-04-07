import math

def calc_gueses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped+1
    return max_guesses


def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed
    if low is None and high is None:
        error = "please enter an integer"
    # if the number needs to be more than an integer
    elif low is not None and high is None:
        error = f"please enter a enter a number that is more than or equal to {low}"

    # if the number needs to be between low and high
    else:
        error = f"please enter a number that is between {low} and {high} (inclusive)"

    # error = "please enter an integer"
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

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
num_rounds = int_check("rounds <enter for infinite>:", low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#get game peramitors
low_num = int_check("low number?")
high_num = int_check("high number?", low= low_num+1)
guesses_allowed = calc_gueses(low_num, high_num)
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
