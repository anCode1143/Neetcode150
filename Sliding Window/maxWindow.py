from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if k == 1:
        return nums
    left, right = 0, k - 1
    answer = []
    currMax = deque()
    for numIndex in range(right+1):
        while (currMax) and (nums[currMax[-1]] < nums[numIndex]):
            currMax.pop()
        currMax.append(numIndex)
    while right < len(nums):
        while currMax and currMax[0] < left:
            currMax.popleft()
        while (currMax) and (nums[currMax[-1]] < nums[right]):
            currMax.pop()
        currMax.append(right)
        answer.append(nums[currMax[0]])
        left += 1
        right += 1
    return answer

print(maxSlidingWindow([1,3,1,2,0,5], 3))