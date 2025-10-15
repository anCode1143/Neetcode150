def exist(self, board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])
    path = set()

    def dfs(row, col, letter_index):
        if letter_index == len(word):
            return True
        elif (row < 0 or row >= ROWS or
            col >= COLS or col < 0 or
            board[row][col] != word[letter_index] or
            (row, col) in path):
            return False
        
        path.add((row, col))
        letter_index += 1
        answer = (
        dfs(row+1, col, letter_index) or 
        dfs(row-1, col, letter_index) or
        dfs(row, col+1, letter_index) or
        dfs(row, col-1, letter_index))
        path.remove((row, col))
        return answer
    

    for col in range(COLS):
        for row in range(ROWS):
            if dfs(row, col, 0):
                return True
    return False
    