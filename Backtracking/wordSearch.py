from typing import List
def exist(self, board: List[List[str]], word: str) -> bool:
    # Looks like dfs but backtrack visited nodes
    ROWS = len(board)
    COLS = len(board[0])
    def inBounds(row, col):
        if 0 <= row < ROWS and  0 <= col < COLS:
            return True
        else: return False
    def backtrack(row, col, visited, wordIndex):
        if wordIndex == len(word):
            return True
        directions = [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]
        for direction in directions:
            if (inBounds(direction[0], direction[1]) and not direction in visited and 
                board[direction[0]][direction[1]] == word[wordIndex]):
                visited.add((direction[0], direction[1]))
                if backtrack(direction[0], direction[1], visited, wordIndex+1):
                    return True
                visited.remove((direction[0], direction[1]))
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word[0]:
                visited = set()
                visited.add((row, col))
                if backtrack(row, col, visited, 1):
                    return True
    return False