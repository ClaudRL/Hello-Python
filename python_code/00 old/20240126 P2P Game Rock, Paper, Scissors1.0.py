#P2P Game: Rock, Paper, Scissors
import getpass
print("Please enter; '1' for Rock； '2' for Paper； '3' for Scissors or 'ok' to quit!")

while True:
  player1_enter = getpass.getpass("Player1 Enter:")
  if player1_enter.lower() == ('ok'):
    print("See you!")
    break

  player2_enter = getpass.getpass("Player2 Enter:")
  if player2_enter.lower() == ('ok'):
    print("See you!")
    break
  
  try:
    if player1_enter == "1":
      print("Player1 : Rock")
    elif player1_enter == "2":
      print("Player1 : Paper")
    elif player1_enter == "3":
      print("Player1 : Scissors")
    if player2_enter == "1":
      print("Player2 : Rock")
    elif player2_enter == "2":
      print("Player2 : Paper")
    elif player2_enter == "3":
      print("Player2 : Scissors")
    result = int(player1_enter) - int(player2_enter)
    if result == 0:
      print("Draw the game!")
    elif str(result) == "-2" or str(result) == "1":
      print("Winner is Player1!")
    elif str(result) == "-1" or str(result) == "2":
      print("Winner is Player2!")
  
  except ValueError:
    print("Invalid input. Please enter '1' or '2' or '3' or 'ok' to quit.")