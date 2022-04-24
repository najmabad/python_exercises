"""Solution to chapter 1, exercise 1: Guessing game"""
import random


def guessing_game():
    """Generate a random integer from 0 to 100 (included).

    Ask the user repeatedly to guess the number.
    Until, the guess is correct, tell the user to guess
    higher or lower.
    """
    answer = random.randint(0, 100)

    while True:   # use this to create an infinite loop
        user_guess = int(input("What is your guess? "))   # placing this inside the loop avoids repetition

        if user_guess == answer:
            print(f"Right! The answer is {answer}")
            break
        elif user_guess < answer:
            print(f"Your guess of {user_guess} is too low!")
        elif user_guess > answer:
            print(f"Your guess of {user_guess} is too high!")
