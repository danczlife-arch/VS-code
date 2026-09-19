import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number:
    print("Correct!")
else:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    other_guess = int(input("That was your first guess! Guess again: "))
    if other_guess == secret_number:
        print("Correct!")
    elif other_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    print("That was your last guess! The secret number was", secret_number)
play_again = input("Do you want to play again? (yes/no): ")