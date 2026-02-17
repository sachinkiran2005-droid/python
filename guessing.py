import random

number = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed in", attempts, "attempts")
        break
