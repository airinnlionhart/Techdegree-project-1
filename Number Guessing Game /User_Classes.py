class Player:

    def __init__(self, high_score, number_of_tries, users_guess):
        self.high_score = high_score
        self.number_of_tries = number_of_tries
        self.users_guess = users_guess

    def get_users_guess(self):
        while True:
            try:
                guess = int(input("Please guess a number between 1 and 10: "))
                if 1 <= guess <= 10:
                    self.users_guess = guess
                    break
                else:
                    print("Number must be an integer between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def update_high_score(self):
        if self.high_score == 0:
            self.high_score = self.number_of_tries
        elif self.number_of_tries < self.high_score:
            self.high_score = self.number_of_tries
        else:
            pass

    @staticmethod
    def restart_game(player):
        restart_game = str(input(
            "Current low score is {} See if you can beat that. Would you like to try again? [Y]es/[N]o: ".format(
                player.high_score)))
        if restart_game.upper() == "Y" or restart_game.upper() == "YES":
            # Reset necessary attributes for a new game
            player.number_of_tries = 0
            player.users_guess = None
            return True
        elif restart_game.upper() == "N" or restart_game.upper() == "NO":
            print("The lowest score of the game was {}".format(player.high_score))
            return False
        else:
            print("Invalid input. Please enter [Y]es or [N]o.")

