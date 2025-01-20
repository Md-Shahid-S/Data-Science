#Simple Number Guessing Game

import random

def num_game():

    secret = random.randint(1,100)
    print("I'm Guessing a Number between 1 to 100")
    attempts = 0

    while True:
        try:
            guess = int(input("Enter Your guess"))
            attempts += 1
            if guess > secret:
                print("Too High Guess")
            elif guess < secret:
                print("Too Low Guess")
            else:
                print(f'You made a correct guess of {secret} in {attempts} attempts')
                break
        except ValueError:
            print('Invalid Number')



#Now calling the function
num_game()