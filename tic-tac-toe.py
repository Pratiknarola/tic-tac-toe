#Tic Tac Toe

import random

def drawBoard(board):
    #this function prints out the board that it was passed

    #"board is a list of 10 strings representing the board(ignore index 0)"
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    #lets the player type which letter they want to be.
    #returns a list with the player's letter as the first item, and 2nd as computer
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        #the first element in the list id the player's letter, the second is the computer's letter
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    #randomly choos the player who goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #this function returns true if the player wamts to play again, otherwise it returns false
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinnner(board, letter):
    #givven a board and a player's letter, this function returns true if that player has won
    #here i used bo instead of board and le instead of letter
    return ((board[7]== letter and board[8]== letter and board[9]== letter) or
            (board[4]== letter and board[5]== letter and board[6]== letter) or
            (board[1]== letter and board[2]== letter and board[3]== letter) or
            (board[7]== letter and board[4]== letter and board[1]== letter) or
            (board[8]== letter and board[5]== letter and board[2]== letter) or
            (board[9]== letter and board[6]== letter and board[3]== letter) or
            (board[7]== letter and board[5]== letter and board[3]== letter) or
            (board[9]== letter and board[5]== letter and board[1]== letter))

def getBoardCopy(board):
    #make a duplicate of the board list and return its duplicate.
    duBoard = []

    for i in board:
        duBoard.append(i)

    return duBoard

def isSpaceFree(board, move):
    #returns true if space is free
    return board[move] == ' '

def getPlayerMove(board):
    #let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    #returns a valid move from the passed list on the passed board.
    #returns none if there is no valid move
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #given a board and the computer's letter
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #here is algorithm for our tic tac toe AI
    #first check if we can win in next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinnner(copy, computerLetter):
                return i

    #check if the player can win in their next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinnner(copy, playerLetter):
                return i

    #try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    #rtry to take center if it is free
    if isSpaceFree(board, 5):
        return 5

    #move on one of the sides.
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is Tie!!')
    else:
        if move != None:
            return move

def isBoardFull(board):
    #return true if every space on the bord has been taken otherwise return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe')

while True:
    #Reset the board
    theBoard = [' '] * 20
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinnner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray!! You have won the game!')
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is Tie!!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            if move == None:
                for i in range(1, 10):
                    if theBoard[i] == ' ':
                        move = int(i)
                        break
            makeMove(theBoard, computerLetter, move)

            if isWinnner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you!! You lose.!!')
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!!!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
