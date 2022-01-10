'''
Assignment 1: Tic-Tac-Toe
Author: Carter Thompson
CSE 210-01
'''

def main():
    gameBoard = createGrid()
    displayGrid(gameBoard)
    turn = 2
    while not checkForWin(gameBoard, turn):
        takeTurn(gameBoard, turn)
        displayGrid(gameBoard)
        turn += 1
    displayWinner(turn)

def createGrid():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return grid

def displayGrid(board):
    print()
    for i in range(3):
        for j in range(3):
            if j == 2:
                endChar = '\n'
            else:
                endChar = '|'
            print(f"{board[i][j]}", end = endChar)
        if i != 2:
            print("-+-+-")
    pass

def takeTurn(board, turn):
    if (turn % 2) != 0:
        print("\n*** O's turn to move! ***")
        doMove(board, turn)
    else:
        print("\n*** X's turn to move! ***")
        doMove(board, turn)

def doMove(board, turn):
    invalid = True
    while invalid:
        move = int(input("Enter the number of the place you want to move: "))
        if checkValidMove(board, move):
            col = (move % 3) - 1
            row = int((move - 1) / 3)
            if turn % 2 == 0:
                board[row][col] = 'x'
            else:
                board[row][col] = 'o'
            invalid = False
        else:
            print("Error! That space is invalid.")


def checkValidMove(board, space):
    for i in range(3):
        for j in range(3):
            if space == board[i][j]:
                return True
    return False

def checkForWin(board, turn):
    if turn < 7:
        pass
    elif turn >= 11:
        return True
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                return True
            elif board[0][i] == board[1][i] == board[2][i]:
                return True
        if board[0][0] == board[1][1] == board[2][2]:
            return True
        if board[2][0] == board[1][1] == board[0][2]:
            return True
    return False

def displayWinner(turn):
    if turn >= 11:
        print("\n*** The game has ended in a draw! ***")
    elif turn % 2:
        print("\n *** Congratulations to our winner, X! ***")
    else:
        print("\n *** Congratulations to our winner, O! ***")

if __name__ == "__main__":
    main()