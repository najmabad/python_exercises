import random

answer = random.randint(0, 100)
trials = 0

while True:
    trials += 1
    if trials > 3:
        print("You didn't guess in time")
        break

    guess = int(input("What is your guess? "))

    if guess == answer:
        print("Right!")
        break
    elif guess < answer:
        print("too low")
    elif guess > answer:
        print("too high")

