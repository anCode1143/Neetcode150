from collections import deque
from typing import List, Set, Tuple

def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
    ROWS = len(board)
    COLS = len(board[0])

    def crushableCandies() -> Set[Tuple[int, int]]:
        # check all rows, for every cell, check if the next 3 cells are the same and not in visited, if so,
            # do bfs on them, adding the whole cluster to the targets
        # check columns the same way
        candies = set()
        for row in range(0, ROWS-2):
            for col in range(COLS):
                if board[row][col] == board[row+1][col] == board[row+2][col] != 0:
                    r = row
                    while r < ROWS and board[r][col] == board[row][col]:
                        candies.add((r, col))
                        r += 1
        for row in range(0, ROWS):
            for col in range(COLS-2):
                if board[row][col] == board[row][col+1] == board[row][col+2] != 0:
                    c = col
                    while c < COLS and board[row][c] == board[row][col]:
                        candies.add((row, c))
                        c += 1
        return candies

    def crushCandies(targets: Set[Tuple[int, int]]):
        for candy in targets:
            board[candy[0]][candy[1]] = 0
        # column by column, count zeros and drop elements accordingly, replace original with 0
        for col in range(COLS):
            zeroes = 0
            for row in range(ROWS-1, -1, -1):
                if board[row][col] == 0:
                    zeroes += 1
                elif zeroes > 0:
                    board[row + zeroes][col] = board[row][col]
                    board[row][col] = 0

    while True:
        targets = crushableCandies()
        if not targets:
            return board
        else:
            crushCandies(targets)