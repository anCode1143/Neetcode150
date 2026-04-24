from collections import deque
from typing import List

def maxDistance(self, grid: List[List[int]]) -> int:
    ROWS = COLS = len(grid)
    queue = deque()
    visited = set()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                queue.append((row, col, 0))
    if not queue or len(queue) == ROWS * COLS: return -1

    answer = -1
    while queue:
        cell = queue.popleft()
        row, col, dist = cell
        paths = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        for path in paths:
            if (path not in visited and 0 <= path[0] < ROWS and 0 <= path[1] < COLS and 
                grid[path[0]][path[1]] == 0):
                visited.add(path)
                queue.append((path[0], path[1], dist+1))
                answer = max(answer, dist+1)
    return answer