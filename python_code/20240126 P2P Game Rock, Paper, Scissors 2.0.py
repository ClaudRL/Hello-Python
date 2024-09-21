#P2P Game: Rock, Paper, Scissors
import getpass
print("Please enter; '1' for Rock； '2' for Paper； '3' for Scissors or 'ok' to quit!")

def play_game(player1,player2):
  #Display the selection
  if player1 == "1":
     print("Player1 : Rock")
  elif player1 == "2":
    print("Player1 : Paper")
  elif player1 == "3":
    print("Player1 : Scissors")
  if player2 == "1":
    print("Player2 : Rock")
  elif player2 == "2":
    print("Player2 : Paper")
  elif player2 == "3":
    print("Player2 : Scissors")
  
  #Judge the Game!
  judge_result = int(player1) - int(player2)
  if judge_result == 0:
    print("Draw the game!")
    return "Draw"
  elif str(judge_result) == "-2" or str(judge_result) == "1": 
    print("Winner is Player1!")
    return "Player1"
  elif str(judge_result) == "-1" or str(judge_result) == "2":
    print("Winner is Player2!")
    return "Player2"
while True:
  #Enter player selection
  player1_enter = getpass.getpass("Player1 Enter:")
  if player1_enter.lower() == ('ok'):
    print("See you!")
    break
  if player1_enter not in ['1','2','3',"ok"]:
    print("Please enter; '1' for Rock； '2' for Paper； '3' for Scissors or 'ok' to quit!")
    continue
  player2_enter = getpass.getpass("Player2 Enter:")
  if player2_enter.lower() == ('ok'):
    print("See you!")
    break
  if player2_enter not in ['1','2','3',"ok"]:
    print("Please enter; '1' for Rock； '2' for Paper； '3' for Scissors or 'ok' to quit!")
    continue
  
  result = play_game(player1_enter,player2_enter)
  #print(f"Result: {result}")
  
  