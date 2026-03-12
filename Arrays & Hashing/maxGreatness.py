from collections import deque
from typing import List

def maximizeGreatness(nums: List[int]) -> int:
    # sort nums, make a queue copy
    # if nums[i] > queue[i], pop, else popleft and answer++
    nums.sort(reverse=True)
    queue = deque(nums)
    answer = 0
    for index in range(len(nums)):
        if nums[index] < queue[0]:
            queue.popleft()
            answer += 1
        else:
            queue.pop()
    return answer

print(maximizeGreatness([1,2,3,4]))