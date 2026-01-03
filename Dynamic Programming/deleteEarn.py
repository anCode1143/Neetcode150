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

"""
cue for diagnosing pattern - tracking future value with past one

how to implement the solution
    init a, b, prevVal and val
    calculate points
    assess if b can take
    calculate recurrence relationship
    shift variables forward

struggled parts
    initialising a and b

complexity details
    speed - linear, goes up to the target from 0, nested loop has the same index updated
    memory - constant, only tracking 2 variables of leading values
"""