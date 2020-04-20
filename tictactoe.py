"""
Tic Tac Toe Player
"""

import math
import copy
from random import randint

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for row in board:
        countX += row.count(X)
        countO += row.count(O)
    if countX <= countO:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    new_board = copy.deepcopy(board)

    if len(action) != 2 or i >= 3 or j >= 3 or new_board[i][j] != EMPTY:
        raise ValueError('Action not possible')  
    else:
        if player(board) == X:
            new_board[i][j] = X
        else:
            new_board[i][j] = O

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    XdiagDown = XdiagUp = OdiagDown = OdiagUp = 0
    for i,row in enumerate(board):
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

        if board[i][i] == X:
            XdiagDown += 1
        if board[i][2-i] == X:
            XdiagUp += 1
        if board[i][i] == O:
            OdiagDown += 1
        if board[i][2-i] == O:
            OdiagUp += 1
    if 3 in [XdiagDown,XdiagUp]:
        return X
    if 3 in [OdiagDown,OdiagUp]:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any( None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerOfRound = winner(board)
    if winnerOfRound == X:
        return 1
    elif winnerOfRound == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    board = copy.deepcopy(board)

    BestScore = -math.inf
    player_name = player(board)

    if terminal(board):return None

    if board == initial_state():
        i, j = randint(0, 2), randint(0, 2)
        return (i, j)
        
    



    if player_name == X:
        value = -math.inf
        move = (-1, -1)
        for action in actions(board):
            minv = MIN_VALUE(result(board, action))
            if minv == 1:
                move = action
                break
            if minv > value:
                value = minv
                move = action
        return move

    if player_name == O:
        value = math.inf
        move = (-1, -1)
        for action in actions(board):
            maxv = MAX_VALUE(result(board, action))
            if maxv == -1:
                move = action
                break
            if maxv < value:
                value = maxv
                move = action
        return move

        


def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
        if v == 1:
            break
    return v

def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))
        if v == -1:
            break
    return v

# print(actions([[EMPTY, X, EMPTY],
#             [X, EMPTY, O],
#             [EMPTY, O, EMPTY]]))
# print(winner([[O, O, O],
#             [EMPTY, O, X],
#             [X, EMPTY, X]]))