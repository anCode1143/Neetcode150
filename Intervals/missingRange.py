from typing import List

def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
    if not nums:
        return [[lower, upper]]
    answer = []
    if nums[0] - lower > 0:
        answer.append([lower, nums[0]-1])
    prev = nums[0]
    for num in nums:
        if num - prev > 1:
                answer.append([prev+1, num-1])
        prev = num
    if  upper - nums[-1] > 0:
        answer.append([nums[-1]+1, upper])
    return answer