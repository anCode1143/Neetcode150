from typing import List
def search(self, nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = ((right - left) // 2) + left
        if nums[middle] == target:
            return True
        if nums[middle] == nums[left] == nums[right]:
            left += 1
            right -= 1
            continue
        if nums[middle] < nums[right]:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        elif nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            right = middle - 1
    return False