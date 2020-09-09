import numpy as np
import time

def numberOfBoards(n):
    row = [1]
    column = [1]
    validBoards = []

    return numberOfBoardsByRowColumn(row, column, 2, n, validBoards), validBoards

def numberOfBoardsByRowColumn(row, column, i, n, validBoards):
    # if the row and column is complete, return 0 or 1 and add the board if valid
    if len(row) == n and len(column) == n:
        if isValid(row, column, n):
            board = get_board(row, column).astype(int) - 1
            validBoards.append(board)
            return 1
        else:
            return 0

    # else if they are not complete but we are over n**2, return 0
    elif i > n**2:
        return 0

    # count the boards
    numBoards = 0

    # recursive case 1: i is in the row
    if len(row) < n:  
        row.append(i)
        if isValid(row, column, n):
            numBoards += numberOfBoardsByRowColumn(row, column, i+1, n, validBoards)
        row.pop()

    # recursive case 2: i is in the column
    if len(column) < n:
        column.append(i)
        if isValid(row, column, n):
            numBoards += numberOfBoardsByRowColumn(row, column, i+1, n, validBoards)
        column.pop()

    # recursive case 3: neither
    numBoards += numberOfBoardsByRowColumn(row, column, i+1, n, validBoards)

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

    n, validBoards = numberOfBoards(6)
    print(n)
    print()
    for board in validBoards:
        print(board)
        print()
    end = time.time()

    print("this took", end-start, "seconds")