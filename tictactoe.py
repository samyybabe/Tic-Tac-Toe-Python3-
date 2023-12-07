import random
from array import *

def printboard(board):#passed
    for i in range(3):
        print(" {} | {} | {}  ".format(board[i][0], board[i][1], board[i][2]))
        if(i<2):
            print("---|---|---")
    print("##############################################")

def createboard():#passed
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    return board

def checkwin(board):#passed
    winner = ''
    #checks wins in rows
    if board[0][0] == board[0][1] == board[0][2] : winner = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] : winner = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] : winner = board[2][0]

    #checks wins in coloumns
    elif board[0][0] == board[1][0] == board[2][0] : winner = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] : winner = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] : winner = board[0][2]
    
    #checks wins in diagonal
    elif board[0][0] == board[1][1] == board[2][2] : winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] : winner = board[0][2]

    print("The winner is {}".format(winner))
    if winner == "X" or winner=="O":
        return True
    else:
        return False
    
def emptypos(board):#passed
    emptyposindex = []
    for i in range(3):
        for j in range (3):
            if board[i][j]==' ':
                emptyposindex.append([i,j])
    return emptyposindex

def compmove(board,emptyposindex):#passed
    pos = random.choice(emptyposindex)
    board[pos[0]][pos[1]] = 'O'
    return board

def playermove(board): #player move always x
    while True:
        rowindex = int(input("Enter Row: "))
        colindex = int(input("Enter Col: "))
        
        if ((rowindex or colindex) >= 0 )and((rowindex or colindex) <= 2):
            break
        print("row and col should be in between(0-2)")
    if board[rowindex][colindex]==' ':
        board[rowindex][colindex] = 'X'
        return board
    else:
        print("invalid move")
        playermove(board)

def main():
    while True:
        board = createboard()
        printboard(board)
        while True:
            playermove(board)
            printboard(board)
            emptyindexs=emptypos(board)
            result=checkwin(board)
            if emptyindexs==[] and result != True:
                print("Tie")
                break
            
            if result==True:
                break
       
            emptyindexs=emptypos(board)
            if emptyindexs==[] and result != True:
                print("Tie")
                break
            compmove(board,emptyindexs)
            printboard(board)

            result=checkwin(board)
            if result==True:
                break

        user_input = input("Play Again? (y/n): ")
        if user_input.lower() != 'y':
            break 

if __name__ == "__main__":
    main()
    

#testing ground