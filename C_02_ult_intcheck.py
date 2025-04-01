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

            return (response)
        except ValueError:
            print(error)

# main routine goes here

# rounds = "test"
# while rounds != "":
#     rounds = int_check("rounds <enter for infinite>: ", low=1, exit_code="")
#     print(f"you asked for {rounds}")

# low_num = int_check("low number?")
# print(f"you chose a low number of {low_num}")
#
# high_num = int_check("high number?", low =1 )
# print(f"you chose a high number of {high_num}")

# check user guesses

guess = ""
while guess != "xxx":
    guess int_check("guess: ", low = 0, high = 10, exit_code="xxx")
    print(f"you guessed {guess}")
    print()
