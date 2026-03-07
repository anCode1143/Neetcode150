from collections import defaultdict
from typing import List

def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
    CENTRE = len(grid) // 2 + 1
    yCells = set()
    yElements = defaultdict(int)
    elseElements = defaultdict(int)
    col = (0, len(grid)-1)
    for row in range(0, CENTRE):
        yCells.add((row, col[0]))
        yCells.add((row, col[1]))
        col = (col[0] + 1, col[1] - 1)
    for row in range(CENTRE, len(grid)):
        yCells.add((row, len(grid) // 2))
    
    for row in range(len(grid)):
        for col in range(len(grid)):
            if (row, col) in yCells:
                yElements[grid[row][col]] += 1
            else:
                elseElements[grid[row][col]] += 1

    sortedY = sorted(yElements.items(), key=lambda x: x[1], reverse=True)
    firstYPair = sortedY[0]
    sortedElse = sorted(elseElements.items(), key=lambda x: x[1], reverse=True)
    firstElsePair = sortedElse[0]
    if sortedY[0][0] == sortedElse[0][0]:
        secondYPair = sortedY[1] if len(sortedY) > 1 else (0, 0)
        secondElsePair = sortedElse[1] if len(sortedElse) > 1 else (0, 0)
        optionOne = (len(yCells) - firstYPair[1]) + (len(grid) * len(grid) - secondElsePair[1] - len(yCells))
        optionTwo = (len(yCells) - secondYPair[1]) + (len(grid) * len(grid) - firstElsePair[1] - len(yCells))
        return min(optionOne, optionTwo)
    else:
        return (len(yCells) - firstYPair[1]) + (len(grid) * len(grid) - firstElsePair[1] - len(yCells))