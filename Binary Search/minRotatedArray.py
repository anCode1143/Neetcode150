from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    min = nums[-1]
    while left <= right:
        middle = ((right - left) // 2) + left
        if nums[middle] > nums[right]:
            left = middle + 1
            min = nums[middle]
        elif nums[middle] < nums[right]:
            right = middle
            min = nums[middle]
        if left == right:
            return nums[left]
    return min

print(findMin([4,5,6,7,0,1,2]))