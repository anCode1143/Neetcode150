from typing import List
from collections import deque
def islandPerimeter(grid: List[List[int]]) -> int:
    # iterate through map finding entry node
    # init visited set
    # run bfs;
    # check adjacent nodes:
        # if land and not in set, run bfs
        # if no land, increment answer
    ROWS = len(grid)
    COLS = len(grid[0])
    def inBounds(row, col) -> bool:
        validRow = row >= 0 and row < ROWS
        validCol = col >= 0 and col < COLS
        return validRow and validCol
    
    start = None
    for row in range(ROWS):
        if start:
            break
        for col in range(COLS):
            if grid[row][col] == 1:
                start = (row, col)
                break

    visited = set()
    visited.add(start)
    queue = deque()
    perimeter = 0
    queue.append(start)
    while queue:
        parents = len(queue)
        for _ in range(parents):
            parent = queue.popleft()
            adjacents = [[parent[0]+1, parent[1]], [parent[0]-1, parent[1]], [parent[0], parent[1]+1], [parent[0], parent[1]-1]]
            for adjacent in adjacents:
                if inBounds(adjacent[0], adjacent[1]) and grid[adjacent[0]][adjacent[1]] == 1 and (adjacent[0], adjacent[1]) not in visited:
                    queue.append(adjacent)
                    visited.add((adjacent[0], adjacent[1]))
                elif not inBounds(adjacent[0], adjacent[1]) or grid[adjacent[0]][adjacent[1]] == 0:
                    perimeter += 1
    return perimeter
            
print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))