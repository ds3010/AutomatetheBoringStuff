theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}

def printBoard(board):
    print(' ')
    print (' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'] + ' ')
    print ('---+---+---')
    print (' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] + ' ')
    print ('---+---+---')
    print (' ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + ' ')
    print(' ')

def modifyBoard(i,player):
    #At this point, the player has indicated their play (i), but they might have indicated a spot that was already played or a spot that does not exist
    #The following block continuously asks the player for a move until a valid one is entered and then modifies the board accordingly
    while (i not in theBoard.keys()) or (theBoard[i] != ' '):
        if i not in theBoard.keys():
            print('There is no spot named ' + i + ', please try again.')
            print(player + '-Player: Type a spot in the board:')
            print('Spots available: ', end='')
            for x in theBoard.keys():
                if theBoard[x] == ' ':
                    print(str(x) + ', ',end='')
            print(' ')
            i = input()
        elif theBoard[i] != ' ':
            print('Spot ' + i + ' has already been played, please try again.')
            print(player + '-Player: Type a spot in the board:')
            print('Spots available: ', end='')
            for x in theBoard.keys():
                if theBoard[x] == ' ':
                    print(str(x) + ', ',end='')
            print(' ')
            i = input()
    #A valid spot has been chosen at this point, so assing that spot a value of X
    theBoard[i] = player

def isAWinner(player):
    #Either an 'X' or a 'O' is used as an argument to see if either player has won, it prints a congratulating message if that is the case and returns a
    #boolean value of TRUE
    if ((theBoard['top-L'] == player and theBoard['top-M'] == player and theBoard['top-R'] == player) or
        (theBoard['mid-L'] == player and theBoard['mid-M'] == player and theBoard['mid-R'] == player) or
        (theBoard['low-L'] == player and theBoard['low-M'] == player and theBoard['low-R'] == player) or
        (theBoard['top-L'] == player and theBoard['mid-L'] == player and theBoard['low-L'] == player) or
        (theBoard['top-M'] == player and theBoard['mid-M'] == player and theBoard['low-M'] == player) or
        (theBoard['top-R'] == player and theBoard['mid-R'] == player and theBoard['low-R'] == player) or
        (theBoard['top-L'] == player and theBoard['mid-M'] == player and theBoard['low-R'] == player) or
        (theBoard['low-L'] == player and theBoard['mid-M'] == player and theBoard['top-R'] == player)):
        print('Congratulations ' + player + '-Player!!!. You have won!!!. Ending the Game')
        return True
    else:
        return False

def isATie():
    #This function evaluates if all spots have been played and returns a value of "TRUE" if that is the case. This function will be applied after evaluating
    #if there is a winner. The program will be terminated if a tie is found
    if ((theBoard['top-L'] != ' ') and (theBoard['top-M'] != ' ') and (theBoard['top-R'] != ' ') and
        (theBoard['mid-L'] != ' ') and (theBoard['mid-M'] != ' ') and (theBoard['mid-R'] != ' ') and
        (theBoard['low-L'] != ' ') and (theBoard['low-M'] != ' ') and (theBoard['low-R'] != ' ')):
        print('This game is a tie!, Ending the Game')
        return True
    else:
        return False

while True:
    #Asking X-player for a spot to play on, this input is evaluated in "modifyBoard" function, and if valid, the change is applied, then we print the board,
    #and evaluate if X-player is a winner
    print(' ')
    print('X-Player: Type a spot in the board:')
    print('Spots available: ', end='')
    for x in theBoard.keys():
        if theBoard[x] == ' ':
            print(str(x) + ', ',end='')
    print(' ')
    xMove = input()
    modifyBoard(xMove, 'X')
    printBoard(theBoard)
    if isAWinner('X'):
        break
    
    #Before the next input, we need to evaluate if there is a tie
    if isATie():
        break

    #Now we do the same for the O-player
    print(' ')
    print('O-Player: Type a spot in the board:')
    print('Spots available: ', end='')
    for o in theBoard.keys():
        if theBoard[o] == ' ':
            print(str(o) + ', ',end='')
    print(' ')
    oMove = input()
    modifyBoard(oMove, 'O')    
    printBoard(theBoard)
    if isAWinner('O'):
        break