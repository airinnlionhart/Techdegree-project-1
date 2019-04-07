"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print('''*********************************************************  
      Welcome to Aaron's Guessing Game 
**********************************************************''')  

    solution = random.randint(1,10)
    number_of_trys = 0 
    while True:
      try:
        check = int(input("Please quess a number between 1 and 10:"))
        if check < 1 or check > 10:
          print("Please choose a number between 1 and 10")
        elif check == solution:
          number_of_trys += 1
          print("You Got It!!!!! It only took you {} number of tries Great           Job!".format(number_of_trys))
          print("**************** Game Over! *******************")
          break
        elif check > solution:
          print("It's lower")
          number_of_trys += 1      
        elif check < solution:
          print("It's Higher")
          number_of_trys += 1      
      except ValueError:
          print("Sorry we where expecting just a number try again")
          


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()