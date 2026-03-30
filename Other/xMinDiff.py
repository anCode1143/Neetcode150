from typing import List
from sortedcontainers import SortedList

def minAbsoluteDifference(nums: List[int], x: int) -> int: 
    # sorted list
    answer = float('inf')
    valid = SortedList()

    for index in range(x, len(nums)):
        valid.add(nums[index-x])
        i = valid.bisect_left(nums[index])
        if i == len(valid) or (i >= 1 and abs(valid[i] - nums[index]) > abs(valid[i-1] - nums[index])):
            i -= 1
        answer = min(answer, abs(valid[i] - nums[index]))
    return int(answer)

print(minAbsoluteDifference([5,3,2,10,15], 1))