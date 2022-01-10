'''
Assignment 1: Tic-Tac-Toe
Author: Carter Thompson
CSE 210-01
'''

def main():
    '''
    main: 
    Calls functions to create and show the starting board, then loops so you can play the game. Calls
    functions to end the game and display the winner, as well.
    '''
    gameBoard = createGrid()
    displayGrid(gameBoard)
    turn = 2
    while not checkForWin(gameBoard, turn):
        takeTurn(gameBoard, turn)
        displayGrid(gameBoard)
        turn += 1
    displayWinner(turn)

def createGrid():
    '''
    createGrid:
    Creates a new game board with spaces 1-9, then returns it.
    '''
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return grid

def displayGrid(board):
    '''
    displayGrid:
    Displays the grid according to the requirements.
        Parameters:
            board - the game board created by createGrid
    '''
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
    '''
    takeTurn:
    Figures out whose turn it is, then prints a statement to tell the user(s) that. Calls doMove
    to select a space to move.
        Parameters:
            board - the game board created by createGrid
            turn - the value in main used to figure out whose turn it is. X always starts.
    '''
    if (turn % 2) != 0:
        print("\n*** O's turn to move! ***")
        doMove(board, turn)
    else:
        print("\n*** X's turn to move! ***")
        doMove(board, turn)

def doMove(board, turn):
    '''
    doMove:
    Puts an 'x' or 'o' in the spot given by the user. Calls checkValidMove first to make sure that's a thing it can do.
        Parameters:
            board - the game board created by createGrid
            turn - the value in main used to figure out whose turn it is. X always starts.
    '''
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
    '''
    checkValidMove:
    Checks if the value given by the user is present and available in the board. Returns True if a 
    match is found, False if not.
        Parameters:
            board - the game board created by createGrid
            space - the number of the space chosen by the user to put their 'x' or 'o'.
    '''
    for i in range(3):
        for j in range(3):
            if space == board[i][j]:
                return True
    return False

def checkForWin(board, turn):
    '''
    checkForWin:
    A slightly misleading name. This really checks if the game is over, but most of the cases
    it looks at would be for wins. Checks if either player has 3 in a row in any form. Also ends
    the game if 9 turns have occurred. Returns True or False to break the loop in main().
        Parameters:
            board - the game board created by createGrid
            turn - the value in main used to figure out whose turn it is. X always starts.
    '''
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
    '''
    Figures out who won depending on whose turn it would be had the game NOT ended.
    Displays a nice little victory message for the winner, or declares a draw.
        Parameters:
            turn - the value in main used to figure out whose turn it is. X always starts.
    '''
    if turn >= 11:
        print("\n*** The game has ended in a draw! ***")
    elif turn % 2:
        print("\n *** Congratulations to our winner, X! ***")
    else:
        print("\n *** Congratulations to our winner, O! ***")

if __name__ == "__main__":
    main()