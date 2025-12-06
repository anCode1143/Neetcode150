from typing import List
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # nested for loop going through every cell and calling dfs on it
    #   keep track of max area
    # have a visit set so you dont revisit cells
    # have a dfs that will traverse the entire land,
    #   passing the area and increasing it until you return the max area
    visited = set()
    answer = 0
    ROWS = len(grid)
    COLS = len(grid[0])
    def dfs(x, y, area):
        if ((x < 0 or y < 0 or x >= ROWS or y >= COLS) 
            or grid[x][y] == 0 or (x, y) in visited):
            return 0
        visited.add((x, y))
        return (1 + dfs(x+1, y, area) + dfs(x-1, y, area) +
        dfs(x, y-1, area) + dfs(x, y+1, area))
    for x in range(ROWS):
        for y in range(COLS):
            answer = max(answer, dfs(x, y, 0))
    return answer

grid = [
    [1, 1],
    [1, 1]
]
print(maxAreaOfIsland(grid))