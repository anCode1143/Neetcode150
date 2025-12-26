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