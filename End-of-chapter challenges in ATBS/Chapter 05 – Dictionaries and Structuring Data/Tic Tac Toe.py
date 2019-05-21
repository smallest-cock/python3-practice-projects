#! /usr/bin/Python3

theBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '}


def printBoard(board):
    print(' ' + board['tl'] + ' | ' + board['tm'] + ' | ' + board['tr'])
    print('---+---+---')
    print(' ' + board['ml'] + ' | ' + board['mm'] + ' | ' + board['mr'])
    print('---+---+---')
    print(' ' + board['ll'] + ' | ' + board['lm'] + ' | ' + board['lr'])


def boardChecker(board, symbol):
    if board['tl'] == symbol and board['tm'] == symbol and board['tr'] == symbol:
        return 'no'
    elif board['ml'] == symbol and board['mm'] == symbol and board['mr'] == symbol:
        return 'no'
    elif board['ll'] == symbol and board['lm'] == symbol and board['lr'] == symbol:
        return 'no'
    elif board['tl'] == symbol and board['ml'] == symbol and board['ll'] == symbol:
        return 'no'
    elif board['tm'] == symbol and board['mm'] == symbol and board['lm'] == symbol:
        return 'no'
    elif board['tr'] == symbol and board['mr'] == symbol and board['lr'] == symbol:
        return 'no'
    elif board['tl'] == symbol and board['mm'] == symbol and board['lr'] == symbol:
        return 'no'
    elif board['tr'] == symbol and board['mm'] == symbol and board['ll'] == symbol:
        return 'no'
    else:
        return 'yes'


turn = 'X'
won = False
leave = False
while leave is False:
    for i in range(9):
        printBoard(theBoard)
        print('\n\nTurn for ' + turn + '. Move on which space?')
        move = input().lower()
        if move not in theBoard:
            print('That\'s not a valid position. You lose your turn..\n')
            move = turn
        theBoard[move] = turn
        go = boardChecker(theBoard, turn)
        if go == 'yes':
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            won = True
            break
    leave = True
print(' ')
printBoard(theBoard)
if won is True:
    print('\n\nCongratulations, ' + turn + "'s win!!!")
else:
    print('\nDraw... Nobody wins.')
