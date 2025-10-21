def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(row, col, visitSet, prevHeight):
        if (row >= ROWS or row < 0 or
            col >= COLS or col < 0 or
            (row, col) in visitSet or
            heights[row][col] < prevHeight):
            return
        visitSet.add((row, col))
        prevHeight = heights[row][col]
        dfs(row+1, col, visitSet, prevHeight)
        dfs(row-1, col, visitSet, prevHeight)
        dfs(row, col+1, visitSet, prevHeight)
        dfs(row, col-1, visitSet, prevHeight)
    
    for col in range(COLS):
        dfs(0, col, pacific, 0)
        dfs(COLS-1, col, atlantic, 0)
    
    for row in range(ROWS):
        dfs(row, 0, pacific, 0)
        dfs(row, COLS-1, atlantic, 0)
    
    answer = []
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) in pacific and (row, col) in atlantic:
                answer.append([row, col])
    return answer