import numpy as np
import time

def getAllFirstRows(numbers, count):
    if count == 2:
        return [[1,2]]
    elif count == len(numbers):
        return [numbers]

    combinations = getAllFirstRows(numbers[:-1], count)
    for new_combination in getAllFirstRows(numbers[:-1], count-1):
        new_combination.append(numbers[-1])
        combinations.append(new_combination)

    return combinations

def getBoard(row, n):
    row = np.array(row)
    board = [row]

    check = np.zeros(n**2 + 1)
    check[0] = 1
    check[row] = 1

    for _ in range(n-1):
        i = np.min(np.where(check == 0))

        new_row = row + i - 1
        if new_row[-1] > n**2 or np.sum(check[new_row]) > 0:
            return None
        board.append(new_row)
        check[new_row] += 1

    return np.array(board)

def numberOfBoards(n):

    # The last number of the row can be at most n^2 - n since 2 is in the row and
    # the last number of the column must be at least n+1 (1, 3, 4, ..., n+1)
    numberPool = [i for i in range(1, n**2-n+1)]
    allFirstRows = getAllFirstRows(numberPool, n)

    boards = []
    for row in allFirstRows:
        board = getBoard(row, n)
        if board is not None: boards.append(board)

    return boards

if __name__ == "__main__":
    start = time.time()
    boards = numberOfBoards(6)
    print(len(boards))
    print()

    for board in boards:
        print(board)
        print()
    end = time.time()

    print("this took", end - start, "seconds")