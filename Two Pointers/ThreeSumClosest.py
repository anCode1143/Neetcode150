from typing import List

def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    answer = float('inf')
    for givenIndex in range(len(nums)):
        low = 0 if givenIndex != 0 else 1
        high = len(nums) - (1 if givenIndex !=len(nums) - 1 else 2)
        currSum = float('inf')
        while low < high:
            currSum = nums[givenIndex] + nums[low] + nums[high]
            if currSum > target:
                high -= 1 if givenIndex != high - 1 else 2
            elif currSum < target:
                low += 1 if givenIndex != low + 1 else 2
            else: # sum == target
                return target
            
            if abs(currSum - target) < abs(target - answer):
                answer = currSum
                
    return answer