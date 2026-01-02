from typing import List
def deleteAndEarn(nums: List[int]) -> int:
    nums.sort()
    a, b = 0, 0
    index = 0
    prevVal = -1
    while index < len(nums):
        points = nums[index]
        while index < len(nums)-1 and nums[index+1] == nums[index]:
            index += 1
            points += nums[index]
        aCandidate = a + points
        bCandidate = b + (points if nums[index] - prevVal > 1 else 0)
        newVal = max(aCandidate, bCandidate)
        a = b
        b = newVal
        prevVal = nums[index]
        index += 1
    return max(a, b)

print(deleteAndEarn([2]))