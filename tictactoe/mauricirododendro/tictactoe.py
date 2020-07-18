import math
import copy
import time
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    

    #start = time.time()
    #print("hello")

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    xcounter = 0
    ocounter = 0
    for row in board:
        xcounter += row.count(X)
        ocounter += row.count(O)

    if xcounter == ocounter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.append([i, j])
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print('Spot already occupied')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns = []
    # Checks rows
    for row in board:
        xcounter = row.count(X)
        ocounter = row.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    # Checks columns
    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)

    for j in columns:
        xcounter = j.count(X)
        ocounter = j.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O

    # Checks diagonals
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    # No winner/tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if board is full or if there is a winner
    empty_counter = 0
    for row in board:
        empty_counter += row.count(EMPTY)
    if empty_counter == 0:
        
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))    #FIXED
            if k > v:
                
                best_move = action
                #if k==0:
                #    break
                v = k
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))    #FIXED
            if k < v:
                
                v = k
                best_move = action
                #if k==0:
                #    break
    return best_move

def max_value(board):
    if terminal(board):
        #end = time.time()
        #print(end - start)
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v    #FIXED

def min_value(board):
    if terminal(board):
        #end = time.time()
        #print(end - start)
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    #FIXED