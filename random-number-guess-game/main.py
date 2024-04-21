import random

random_number = random.randint(1, 100)
guess_count = 0


while True:
    guess = float(input("Guess a number between 1 and 100: "))
    guess_count += 1

    if guess > random_number:

        print("Guess lower than the number")
    elif guess < random_number:

        print("Guess higher than the number")
    else:
        print("You Win! in the {}.guesses".format(guess_count))
        break