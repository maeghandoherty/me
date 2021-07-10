"""Set 3, Exercise 3.
Steps on the way to making your own guessing game.
"""

import random


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    message = f"give me a number between {low}, and {high}: "

    while True:
        attempt = input(message)
        try:
            input_number = int(attempt)
            if low <= input_number < high:
                # print(f"Nice! {input_number} looks good")
                return input_number
            else:
                # print(f"{input_number} isn't between {low}, and {high}")
                pass
        except Exception as e:
            print("that wasn't a number", e, attempt, "xxx")


def advancedGuessingGame():
    """Play a guessing game with a user.
    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)
    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    good = False
    # while not good:
    print("Enter a lower bound")
    lowerBound = super_asker(-10000000, 1000000)
    print("Enter an upper bound")
    upperBound = super_asker(lowerBound + 2, 1000000)
    print(f"OK then, a number between {lowerBound} and {upperBound} ?")

    actualNumber = random.randint(lowerBound, upperBound - 1)

    guessed = False

    while True:
        print("Guess a number")
        guessedNumber = super_asker(lowerBound, upperBound)
        print(f"You guessed {guessedNumber}")
        if guessedNumber == actualNumber:
            print(f"You got it!! it was {actualNumber}")
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too small :(( Try again !!")
        else:
            print("Too big :(( try again !!")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
