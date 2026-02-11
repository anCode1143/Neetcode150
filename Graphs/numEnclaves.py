from collections import deque
from typing import List
def numEnclaves(self, grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    queue = deque()
    visited = set()

    def isValid(cell):
        if (0 <= cell[0] < ROWS and 0 <= cell[1] < COLS
            and grid[cell[0]][cell[1]] == 1 and not cell in visited):
            return True
        else: return False

    for row in range(ROWS):
        if grid[row][0] == 1 and not (row, 0) in visited:
            queue.append((row, 0))
            visited.add((row, 0))
        if grid[row][COLS-1] == 1 and not (row, COLS-1) in visited:
            queue.append((row, COLS-1))
            visited.add((row, COLS-1))
    for col in range(COLS-1):
        if grid[0][col] == 1 and not (0, col) in visited:
            queue.append((0, col))
            visited.add((0, col))
        if grid[ROWS-1][col] == 1 and not (ROWS-1, col) in visited:
            queue.append((ROWS-1, col))
            visited.add((ROWS-1, col))
    
    while queue:
        cell = queue.popleft()
        grid[cell[0]][cell[1]] = 0
        neighbours = [(cell[0]+1, cell[1]), (cell[0], cell[1]+1), 
                    (cell[0]-1, cell[1]), (cell[0], cell[1]-1)]
        for neighbour in neighbours:
            if isValid(neighbour):
                queue.append(neighbour)
                visited.add(neighbour)

    answer = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                answer += 1
    return answer