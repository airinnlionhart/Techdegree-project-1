import random
from User_Classes import Player

def start_game():
    print('''*********************************************************  
          Welcome to Aaron's Guessing Game 
    **********************************************************''')

    while True:
        solution = random.randint(1, 10)
        user = Player(high_score=0, number_of_tries=0, users_guess=None)

        while True:
            try:
                user.get_users_guess()
                if user.users_guess == solution:
                    user.number_of_tries += 1
                    print("You guessed it!")
                    user.update_high_score()
                    break  # Exit the inner loop when the correct guess is made
                elif user.users_guess > solution:
                    user.number_of_tries += 1
                    print("You're on the right track, but the value is lower. Guess again.")
                else:
                    user.number_of_tries += 1
                    print("You're on the right track, but the value is higher. Guess again.")
            except ValueError:
                print("Sorry, we were expecting just a number. Try again.")

        if not user.restart_game(user):
            print("********************* Game Over **********************************")
            break  # Exit the outer loop when the user decides not to restart


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
