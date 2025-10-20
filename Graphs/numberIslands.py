def numIslands(self, grid: List[List[str]]) -> int:
    seen = set()
    answer = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(row, col):
        if (row >= 0 and row < ROWS and
            col >= 0 and col < COLS and 
            (row, col) not in seen and 
            grid[row][col] == "1"):

            seen.add((row, col))
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

    for col in range(COLS):
        for row in range(ROWS):
            if grid[row][col] == "1" and (row, col) not in seen:
                dfs(row, col)
                answer += 1
    return answer