"""
Tic Tac Toe Player
"""

import math
import copy

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
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    for i in range(3):
        if board[i][0] == X or board[i][1] == X or board[i][2] == X:
            return X
        if board[i][0] == O or board[i][1] == O or board[i][2] == O:
            return O
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

# print(actions([[EMPTY, X, EMPTY],
#             [X, EMPTY, O],
#             [EMPTY, O, EMPTY]]))
# print(result([[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]],(2,2)))