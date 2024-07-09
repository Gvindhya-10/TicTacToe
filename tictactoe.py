board=["_" ,"_","_",
       "_","_","_",
       "_","_","_"]
winner=None
current_player="X"
gameRunning=True
import random

def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("---------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("---------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def playerinput(board):
    global current_player
    inp=int(input("Enter the position from 1 to 9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="_":
        board[inp-1]=current_player
    else:
        print("Invalid input")

def horizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="_" :
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[4]!="_":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[7]!="_":
        winner=board[6]
        return True
    else:
        return False

def vertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="_":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="_":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="_":
        winner=board[2]
        return True
    else:
        return False


def diagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="_":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="_":
        winner=board[2]
        return True
    
    else:
        return False

def checkwinner(board):
    if horizontal(board) or vertical(board) or diagonal(board):
        print("The winner is ",winner)
    else:
        return False


def checktie(board):
    global gameRunning
    if "_" not in board:
        gameRunning=false
        print("It's a tie")

def flipplayer():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"

def computerinput(board):
    while current_player=="O":
        inp=random.randint(0,8)
        if board[inp]=="_":
            board[inp]=current_player
            flipplayer()


def playerinput1(board):
    global current_player
    inp=int(input("Enter the position from 1 to 9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="_":
        board[inp-1]=current_player
    else:
        print("Invalid input")


while gameRunning:
    printboard(board)
    playerinput(board)
    checkwinner(board)
    checktie(board)
    flipplayer()
    playerinput1(board)
    checkwinner(board)
    checktie(board)
    flipplayer()
    


