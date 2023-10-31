#!/usr/bin/python3
"""Solves the N-queens puzzle.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for rows in range(len(board)):
        for columns in range(len(board)):
            if board[rows][columns] == "Q":
                solution.append([rows, columns])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played."""
    for columns in range(col + 1, len(board)):
        board[row][columns] = "x"
    for columns in range(col - 1, -1, -1):
        board[row][columns] = "x"
    for rows in range(row + 1, len(board)):
        board[rows][col] = "x"
    for rows in range(row - 1, -1, -1):
        board[rows][col] = "x"
    columns = col + 1
    for rows in range(row + 1, len(board)):
        if columns >= len(board):
            break
    board[rows][columns] = "x"
    columns += 1
    columns = col - 1
    for rows in range(row - 1, -1, -1):
        if columns < 0:
            break
        board[rows][columns]
        columns -= 1
    columns = col + 1
    for r in range(row - 1, -1, -1):
        if columns >= len(board):
            break
        board[rows][columns] = "x"
        columns += 1
    columns = col - 1
    for rows in range(row + 1, len(board)):
        if columns < 0:
            break
        board[rows][columns] = "x"
        columns -= 1

    def recursive_solve(board, row, queens, solutions):
        """Recursively solve an N-queens puzzle.

        Args:
            board (list): The current working chessboard.
            row (int): The current working row.
            queens (int): The current number of placed queens.
            solutions (list): A list of lists of solutions.
        Returns:
            solutions
        """
        if queens == len(board):
            solutions.append(get_solution(board))
            return (solutions)

        for columns in range(len(board)):
            if board[row][columns] == " ":
                tmp_board = board_deepcopy(board)
                tmp_board[row][columns] = "Q"
                xout(tmp_board, row, columns)
                solutions = recursive_solve(tmp_board, row + 1,
                                            queens + 1, solutions)
        return (solutions)

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)

        board = init_board(int(sys.argv[1]))
        solutions = recursive_solve(board, 0, 0, [])
        for sl in solutions:
            print(sl)
