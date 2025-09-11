def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
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

print(search([5], 5))