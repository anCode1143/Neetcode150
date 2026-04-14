from typing import List

def closedIsland(self, grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    def dfs(node):
        grid[node[0]][node[1]] = 1
        paths = [(node[0]+1, node[1]), (node[0]-1, node[1]), 
                (node[0], node[1]+1), (node[0], node[1]-1),]
        for path in paths:
            if 0 <= path[0] < ROWS and 0 <= path[1] < COLS and grid[path[0]][path[1]] == 0:
                dfs(path)

    for col in range(COLS):
        if grid[0][col] == 0:
            dfs((0, col))
        if grid[ROWS-1][col] == 0:
            dfs((ROWS-1, col))
    for row in range(ROWS):
        if grid[row][0] == 0:
            dfs((row, 0))
        if grid[row][COLS-1] == 0:
            dfs((row, COLS-1))
    
    answer = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                answer += 1
                dfs((row, col))
    return answer