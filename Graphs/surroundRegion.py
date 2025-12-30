from typing import List


def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # go through edges with O, run dfs marking them all safe "S"
    # run through the graph marking all Os as X
    # run through all Ss marking them as O

    ROWS = len(board)
    COLS = len(board[0])

    def markConnectedDFS(row, col, isChar, toChar, visited):
        if inBounds(row, col) and board[row][col] == isChar and (row, col) not in visited:
            board[row][col] = toChar
            visited.add((row, col))
            markConnectedDFS(row+1, col, isChar, toChar, visited)
            markConnectedDFS(row-1, col, isChar, toChar, visited)
            markConnectedDFS(row, col+1, isChar, toChar, visited)
            markConnectedDFS(row, col-1, isChar, toChar, visited)
    
    def inBounds(row, col):
        rowInBounds = False
        colInBounds = False
        if row >= 0 and row < ROWS:
            rowInBounds = True
        if col >= 0 and col < COLS:
            colInBounds = True
        return rowInBounds and colInBounds
    
    visited = set()
    for index in range(ROWS):
        markConnectedDFS(index, 0, "O", "S", visited) # left
        markConnectedDFS(index, COLS-1, "O", "S", visited) # right
    
    for index in range(COLS):
        markConnectedDFS(0, index, "O", "S", visited) # top
        markConnectedDFS(ROWS-1, index, "O", "S", visited) # bottom
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O":
                board[row][col] = "X"
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "S":
                board[row][col] = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


"""
cue for diagnosing pattern - same as pacific atlantic flow, dfs from edges, wanna keep that pattern in mind

how to implement the solution
    spread nodes from edges and save if condition is met
        edges are iterated with two for loops

struggled parts - gotta be careful with the indices

improvement from standard solution
    couldve checked Os and Ss in the same iteration

complexity details
    time - M*N linear, all nodes are visited in constant time, through dfs and later through iterations
    memory - M*N linear, through recursive call stack, worst case iterates through the entire matrix
"""