def adventure_game():
  print("Welcome to the 'Vikings and Pirates: A Lord of the Rings Adventure' game!")

  # First decision: Crossroad
  choice1 = input("You're at a mystical crossroad in Middle-Earth. Where do you want to go? Type 'left' or 'right': ").lower()
  if choice1 == 'left':
      # Second decision: Lake
      choice2 = input("You've come to an ancient lake guarded by a Viking spirit. There is an island in the middle of the lake. Type 'wait' to wait for a Viking longboat. Type 'swim' to swim across: ").lower()
      if choice2 == 'wait':
          # Third decision: House with doors
          choice3 = input("You arrive at the island unharmed. There is a mystical house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
          if choice3 == 'red':
              print("It's a room full of fire. Game Over.")
          elif choice3 == 'yellow':
              print("You found the hidden treasure! You Win!")
          elif choice3 == 'blue':
              print("You enter a room of beasts. Game Over.")
          else:
              print("You chose a door that doesn't exist. Game Over.")
      elif choice2 == 'swim':
          print("You get attacked by an angry sea serpent. Game Over.")
      else:
          print("That's not a valid choice. Game Over.")
  elif choice1 == 'right':
      print("You encounter a band of pirates led by an undead captain. Game Over.")
  else:
      print("That's not a valid choice. Game Over.")

# Start the game
adventure_game()
