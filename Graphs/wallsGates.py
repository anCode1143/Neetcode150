from collections import deque
from typing import List
def islandsAndTreasure(self, grid: List[List[int]]) -> None:

    # iterate through all treasures at the same time
    ROWS, COLS = len(grid), len(grid[0])
    treasures = []
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                treasures.append(deque([(row, col, 0)]))

    def isIncludable(row, col):
        if (row >= 0 and row < ROWS and col >= 0 and col < COLS
            and grid[row][col] == 2147483647):
            return True
        else:
            return False
    
    altered = True
    # while altered, if queue:
        # take parent length, for _ in range(parentLength):
            # popleft = parent, if adj cells not out of bounds and equals inf, 
                # add cells & change values
    while altered:
        altered = False
        for queue in treasures:
            if queue:
                altered = True
                parentLength = len(queue)
                for _ in range(parentLength):
                    parent = queue.popleft()
                    if isIncludable(parent[0]+1, parent[1]):
                        queue.append((parent[0]+1, parent[1], parent[2]+1))
                        grid[parent[0]+1][parent[1]] = parent[2]+1

                    if isIncludable(parent[0]-1, parent[1]):
                        queue.append((parent[0]-1, parent[1], parent[2]+1))     
                        grid[parent[0]-1][parent[1]] = parent[2]+1               

                    if isIncludable(parent[0], parent[1]+1):
                        queue.append((parent[0], parent[1]+1, parent[2]+1))
                        grid[parent[0]][parent[1]+1] = parent[2]+1

                    if isIncludable(parent[0], parent[1]-1):
                        queue.append((parent[0], parent[1]-1, parent[2]+1))
                        grid[parent[0]][parent[1]-1] = parent[2]+1






