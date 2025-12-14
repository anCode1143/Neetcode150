from collections import deque
def orangesRotting(self, grid: List[List[int]]) -> int:
    # iterate the entire matrix to find all rotten oranges, push them to a queue
    # enter a while queue loop, popping old cells and pushing new ones
    # return the amount of iterations made
    rottingOranges = deque()
    iterations = 0
    freshOranges = set()
    ROWS = len(grid)
    COLS = len(grid[0])
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 2:
                rottingOranges.append([row, col])
            elif grid[row][col] == 1:
                freshOranges.add((row, col))
    
    while rottingOranges:
        oranginals = len(rottingOranges)
        for _ in range(oranginals):
            currOrange = rottingOranges.popleft()
            if currOrange[0]+1 < ROWS and grid[currOrange[0]+1][currOrange[1]] == 1:
                grid[currOrange[0]+1][currOrange[1]] = 2
                rottingOranges.append([currOrange[0]+1, currOrange[1]])
                freshOranges.remove((currOrange[0]+1, currOrange[1]))

            if currOrange[0]-1 >= 0 and grid[currOrange[0]-1][currOrange[1]] == 1:
                grid[currOrange[0]-1][currOrange[1]] = 2
                rottingOranges.append([currOrange[0]-1, currOrange[1]])               
                freshOranges.remove((currOrange[0]-1, currOrange[1]))
            
            if currOrange[1]-1 >= 0 and grid[currOrange[0]][currOrange[1]-1] == 1:
                grid[currOrange[0]][currOrange[1]-1] = 2
                rottingOranges.append([currOrange[0], currOrange[1]-1])
                freshOranges.remove((currOrange[0], currOrange[1]-1))
                        
            if currOrange[1]+1 < COLS and grid[currOrange[0]][currOrange[1]+1] == 1:
                grid[currOrange[0]][currOrange[1]+1] = 2
                rottingOranges.append([currOrange[0], currOrange[1]+1])
                freshOranges.remove((currOrange[0], currOrange[1]+1))
        if rottingOranges:
            iterations += 1

    return iterations if not freshOranges else -1
