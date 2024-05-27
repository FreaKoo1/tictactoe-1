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


def player_move(board):
    while True:
      inp = int(input("Please select a number[1-9]: "))
      if inp > 0 and inp < 10 and board[inp -1] == "-":
        board[inp - 1] = player
        break
            
      else:
        print("Invalid movement")
        
while(winner == None and freespace ):
    printboard(board)
    player_move(board)