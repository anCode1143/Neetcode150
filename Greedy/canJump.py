from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    
    validDest = len(nums)-1
    for index in range(len(nums)-2, -1, -1):
        if nums[index] >= validDest - index:
            validDest = index
    return validDest == 0

print(canJump([3,0,8,2,0,0,1]))
            