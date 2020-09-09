import numpy as np
import pdb
import time

def numberOfBoards(n):
    # initialize board
    board = np.array([[1]])
    validBoards = []

    # check array
    check = np.zeros(n**2 + 1)
    check[1] = 1

    return numberOfBoardsIncluding(board, 2, n, check, validBoards), validBoards

def numberOfBoardsIncluding(board, i, n, check, validBoards):
    ''' assumes that board is valid '''

    # if the board is complete, add and return
    if board.shape == (n, n):
        validBoards.append(board.copy())
        return 1

    # else if i too large, return
    if i > n**2:
        return 0
        
    # count the boards
    numBoards = 0

    # recursive case 1: i is in the column
    if board.shape[0] < n:
        # calculate the row
        row = board[0:1, :] + i - 1
        # check if any of them already exist
        if row[0, -1] <= n**2 and np.sum(check[row]) == 0:
            check[row] += 1
            new_board = np.concatenate([board, row], axis=0)
            # pdb.set_trace()
            numBoards += numberOfBoardsIncluding(new_board, i+1, n, check, validBoards)
            check[row] -= 1

    # recursive case 2: i is in the row
    if board.shape[1] < n:
        # calculate the row
        column = board[:, 0:1] + i - 1
        # check if any of them already exist
        if column[-1, 0] <= n**2 and np.sum(check[column]) == 0:
            check[column] += 1
            new_board = np.concatenate([board, column], axis=1)
            # pdb.set_trace()
            numBoards += numberOfBoardsIncluding(new_board, i+1, n, check, validBoards)
            check[column] -= 1

    # recursive case 3: neither
    numBoards += numberOfBoardsIncluding(board, i+1, n, check, validBoards)

    # return
    return numBoards


def isValid(row, column, n):
    # if it goes over n**2 return false immediately
    if row[-1] + column[-1] - 1 > n**2:
        return False

    # get the board
    board = get_board(row, column)

    # check if the board is valid
    return np.unique(board).size == len(row) * len(column)

def get_board(row, column):
    # get numpy vectors from arrays
    rowVector = np.exp([row])
    columnVector = np.exp([column]).T

    # calculate the board
    board = np.dot(columnVector, rowVector)

    # take log and return
    return np.log(board)

if __name__ == "__main__":
    start = time.time()
    
    n, validBoards = numberOfBoards(5)
    print(n)
    print()
    for board in validBoards:
        print(board)
        print()
    end = time.time()

    print("this took", end-start, "seconds")