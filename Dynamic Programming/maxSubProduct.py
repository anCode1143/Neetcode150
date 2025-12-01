def maxProduct(self, nums: List[int]) -> int:
    currMin, currMax = 1, 1
    res = max(nums)
    for number in nums:
        if number == 0:
            currMin, currMax = 1, 1

        temp = currMax
        currMax = max(currMax*number, currMin*number, number)
        currMin = min(temp*number, currMin*number, number)
        res = max(res, currMax)
    return res