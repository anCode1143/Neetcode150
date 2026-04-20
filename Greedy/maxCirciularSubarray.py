from typing import List

def maxSubarraySumCircular(self, nums: List[int]) -> int:
    currMax, currMin = nums[0], nums[0]
    globalMax, globalMin = nums[0], nums[0]
    for elementIndex in range(1, len(nums)):
        currMax = max(nums[elementIndex], currMax + nums[elementIndex])
        currMin = min(nums[elementIndex], currMin + nums[elementIndex])
        globalMax = max(globalMax, currMax)
        globalMin = min(globalMin, currMin)
    if globalMax < 0:
        return globalMax
    else:
        return max(globalMax, sum(nums) - globalMin)