import random

print('''*********************************************************  
      Welcome to Aaron's Guessing Game 
**********************************************************''')  

best_score = 10

def start_game():
    global best_score
    solution = random.randint(1,10)
    number_of_trys = 0 
    while True:
      try:
        check = int(input("Please quess a number between 1 and 10:"))
        if check < 1 or check > 10:
          print("Please choose a number between 1 and 10")
        elif check == solution:
          number_of_trys += 1
          print("You Got It!!!!! It only took you {} number of tries Great Job!".format(number_of_trys))
          if number_of_trys < best_score:
            best_score = number_of_trys
            return best_score             
          break
        elif check > solution:
          print("It's lower")
          number_of_trys += 1      
        elif check < solution:
          print("It's Higher")
          number_of_trys += 1      
      except ValueError:
          print("Sorry we where expecting just a number try again")
def play_agin():
  
  while True :
    try:
      restart_game = str(raw_input("Current low score is {} See if you can beat that would you like you try agin [Y]es/[N]o: ".format(best_score)))  
      if restart_game.upper() == "Y" or restart_game.upper() == "YES":
          start_game()
      elif restart_game.upper() == "N" or restart_game.upper() == "NO":
          print("The lowest score of the game was {}".format(best_score))
          print("********************* Game Over **********************************")
          break 
      else:
          print("Opps we where expecting a Y for Yes or a  N for No")       
    except Exception as e:
      raise e
        

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    play_agin()