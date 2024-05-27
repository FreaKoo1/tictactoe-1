board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
player = "X"
winner = None
response = None
freespace = True

def printboard(board):
    print(board[0]," | ",board[1]," | ",board[2])
    print("-------------")
    print(board[3]," | ",board[4]," | ",board[5])
    print("-------------")
    print(board[6]," | ",board[7]," | ",board[8])


def player_move():
    while True:
      inp = int(input("Please select a number[1-9]: "))
      if inp > 0 and inp < 10 and board[inp -1] == "-":
        board[inp - 1] = player
        break
            
      else:
        print("Invalid movement")
        
    
def checkrow():

 #check horizontel row
  if board[0] == board[1] == board[2] and board[0] != "-":
     return board[0]
  elif board[3] == board[4] == board[5] and board[3] != "-":
     return board[3]
  elif board[6] == board[7] == board[8] and board[6] != "-":
     return board[6]
  return None
def check_columb():
   #check columnb
   if board[0] == board[3] == board[6] and board[0] != "-":
      return board[0]
   elif board[1] == board[4] == board[7] and board[1] != "-":
      return board[1]
   elif board[2] == board[5] == board[8] and board[2] != "-":
      return board[2]
   return None
def check_diagonal():
  
   if board[0] == board[4] == board[8] and board[0] != "-":
      return board[0]
   elif board[2] == board[4] == board[6] and board[2] != "-":
      return board[2]
   return None
def check_winner():
   global winner
   row = checkrow()
   columb = check_columb()
   diagonal = check_diagonal()
   print(row)
   if row:
      winner = row  
   elif columb:
      winner = columb
   elif diagonal:
      winner = diagonal
   print(winner)
    
   
  
def check_tie():
   global freespace
   if "-" not in board:
      freespace = False
      
      print("The game is tied")

def switchPlayer():
   global player
   if player == "X":
      player = "O"
   else:
      player = "X"
import random
def computer_move():
   while player == "O":
     inp = random.randint(0,8)
     if board[inp] == "-":
        board[inp] = "O"
        switchPlayer()
while True :
   printboard(board)
   player_move()
   check_winner()
   check_tie()
   if winner != None or not freespace:
      break
   switchPlayer()
   computer_move()
   check_winner()
   check_tie()
   if winner != None or not freespace:
      break
printboard(board)
print(f"winner is {winner}")
      