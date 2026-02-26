# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def isValid(topInput, bottomInput):
            return topInput.x >= bottomInput.x and topInput.y >= bottomInput.y
        answer = 0
        def recursion(topRight, bottomLeft):
            nonlocal answer
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                if sea.hasShips(topRight, bottomLeft):
                    answer += 1
                return
            verticalMiddle = (topRight.x + bottomLeft.x) // 2
            horizontalMiddle = (topRight.y + bottomLeft.y) // 2
            quadrants = [
                [Point(verticalMiddle, topRight.y), Point(bottomLeft.x, horizontalMiddle + 1)],   # 1
                [topRight, Point(verticalMiddle + 1, horizontalMiddle + 1)],                      # 2
                [Point(verticalMiddle, horizontalMiddle), bottomLeft],                            # 3
                [Point(topRight.x, horizontalMiddle), Point(verticalMiddle + 1, bottomLeft.y)]    # 4
            ]
            for quadrant in quadrants:
                if isValid(quadrant[0], quadrant[1]) and sea.hasShips(quadrant[0], quadrant[1]):
                    recursion(quadrant[0], quadrant[1])
        recursion(topRight, bottomLeft)
        return answer