from typing import List
def searchRotate(nums: List[int], target: int) -> int:
    if nums[0] > nums[-1]: # if rotated
        pivot = findMin(nums)
        if target == nums[pivot]:
            return pivot
        if target > nums[len(nums)-1]:
            return binarySearch(nums[0:pivot], target)
        else:
            if binarySearch(nums[pivot:len(nums)], target) != -1:
                return binarySearch(nums[pivot:len(nums)], target) + pivot
            else:
                return binarySearch(nums[pivot:len(nums)], target)
    else:
        return binarySearch(nums, target)

def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1
    while left <= right:
        middle = ((right - left) // 2) + left
        if target > nums[middle]:
            left = middle + 1
        if target < nums[middle]:
            right = middle - 1
        if target == nums[middle]:
            return middle
    return -1

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    min = nums[len(nums)-1]
    while left <= right:
        middle = ((right - left) // 2) + left
        if nums[middle] > nums[right]:
            left = middle + 1
            min = middle
        elif nums[middle] < nums[right]:
            right = middle
            min = middle
        if left == right:
            return left
    return min

print(searchRotate([3, 1], 0))  