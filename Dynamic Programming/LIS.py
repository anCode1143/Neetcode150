def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)

    for index in range(len(nums)-1, -1, -1):
        for backStep in range(index+1, len(nums)):
            if nums[index] < nums[backStep]:
                dp[index] = max(dp[index], 1 + dp[backStep])
    return max(dp)