class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        potentialAnswers = []
        for index in range(len(grid)):
            sortedRow = sorted(grid[index])
            for _ in range(limits[index]):
                potentialAnswers.append(sortedRow.pop())
            
        potentialAnswers.sort()
        
        answer = 0
        for _ in range(k):
            answer += potentialAnswers.pop()
        return answer