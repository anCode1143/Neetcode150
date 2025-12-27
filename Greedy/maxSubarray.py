def maxSubArray(self, nums: List[int]) -> int:
    # iterate through the array keeping track of currsum and maxsum
    # if currsum < 0, reset
    currSum = 0
    maxSum = 0
    for num in nums:
        currSum += num
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    if maxSum == 0 and 0 not in nums:
        return max(nums)
    return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
    

"""
cue for diagnosing pattern - linear solution in dp-eque problem

how to implement the solution - iterate through the array, reset the value if value is negative

struggled parts - whats the reset value

complexity details
    speed - linear, iterates array
    memory - O(1)
"""