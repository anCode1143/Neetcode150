from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    valueToIndex = {}
    for index in range(len(nums)):
        if nums[index] in valueToIndex:
            if index - valueToIndex[nums[index]] <= k:
                return True
        valueToIndex[nums[index]] = index
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))