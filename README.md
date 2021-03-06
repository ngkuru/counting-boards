### Counting Boards

This repository contains the code which verifies the result from "Counting with the Aid of Cyclotomic Polynomials, Cicek, under revision." The problem goes:

In how many ways can the numbers $1, 2,\ldots , n^2$ be placed on an $n\times n$ board, such that, the sum any $n$ squares, no two of which are on the same row or column, is the same?

This code generates such boards with the additional property that the first two numbers in the board are 1 and 2, and it can be seen that all other boards can be generated by transposing rows/columns and symmetry.

There are four different implementations:

1) construct_from_row
2) construct_from_row_symmetry
3) check_from_row_column
4) append_rows_columns

# construct_from_row

This is the fastest guaranteed implementation of the solution. On a regular notebook, it solves the $n=6$ case in 1 second. It uses the fact that the first row uniquely determines the board, and provides an algorithm to construct it. Then, it checks for valid boards using all possible first rows (increasing $n$ numbers none of which exceed $n^2 - n$).

# construct_from_row_symmetry

This is the fastest implementation, solving the $n=6$ case in 0.04 seconds and the $n=10$ case in 120 seconds. It is the same as construct_from_row except that it assumes a symmetry in the first row when generating possible first rows, i.e. $row_i + row{-i}$ is the same for all $i$.

# check_from_row_column

This implementation solves the $n=6$ case in 180 seconds. It uses the fact that the sum opposing corners of any rectangle consisting of four squares is equal to each other, and checks for valid boards using the first row and column.

# append_rows_columns

This implementation solves the $n=6$ case in 200 seconds. This uses the same method as check_from_row_column, except that it adds whole rows and columns when checking instead of constructing the board after with the first row/column.

# Use

The scripts are hardcoded to solve the $n=6$ case. You can change it to any number, and then run

```python codename.py```

in the directory to get the result.