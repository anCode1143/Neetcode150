from typing import List

def largestRectangleArea(self, heights: List[int]) -> int:
    # create monotonic stack
    # when bar < stack[-1], pop contents until false, calculating each area with index
    # track index for new bar to append
    # calculate remaining areas in stack

    stack = []
    maxRec = 0
    for barIndex in range(len(heights)):
        if stack and heights[barIndex] < stack[-1][1]:
            newIndex = 0
            while stack and heights[barIndex] < stack[-1][1]:
                goneIndex, goneHeight = stack.pop()
                newIndex = goneIndex
                area = (barIndex - goneIndex) * goneHeight
                maxRec = max(maxRec, area)
            stack.append((newIndex, heights[barIndex]))
        else:
            stack.append((barIndex, heights[barIndex]))
    
    for index, value in stack:
        maxRec = max(maxRec, (len(heights) - index) * value)
    return maxRec
    # [5,4,1,2]
    #  0 1 2 3