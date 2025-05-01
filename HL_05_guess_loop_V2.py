def int_check(question, low=None, high=None, exit_code=None):
    """Checks users enter an integer (optional exit code and high / low values)"""
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


secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5
guesses_used = 0

already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:
    guess = int_check("guess", low_num, high_num, )
    if guess == "xxx":
        end_game = "yes"
        break

    if guess in already_guessed:
        print(f"you've already guessed {guess}, you've *still* used "
              f"{guesses_used}/{guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback: str = (f"to low, please try a higher number, "
                         f"you've used {guesses_used}/{guesses_allowed} guesses")

    elif guess > secret and guesses_used < guesses_allowed:

        feedback = (f"to  high, please try a lower number, "
                    f"you've used {guesses_used}/{guesses_allowed} guesses")

    elif guess == secret and guesses_used < guesses_allowed:
        if guesses_used == 1:
            feedback = "🍀🍀🍀lucky! you got it first try!🍀🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = "phew! you got it on the last guess"
        else:
            feedback = f"you go the secret number in {guesses_used}/{guesses_allowed} guesses"

    elif guesses_used == guesses_allowed:
        feedback = "sorry. you ran out of guesses. you lose"

    else:
        feedback = "hello"

    print(feedback)

    if guesses_used == guesses_allowed - 1:
        print("\n💣💣💣careful, you have one guess left!💣💣💣\n")

print()
print("end of round")
