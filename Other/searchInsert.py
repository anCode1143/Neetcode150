class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = ((right - left) // 2) + left
            if target > nums[middle]:
                    left = middle + 1
            elif target < nums[middle]:
                    right = middle - 1
            elif nums[middle] == target:
                    return middle
                    
        if nums[left] < target:
            return left + 1
        else:
            return left