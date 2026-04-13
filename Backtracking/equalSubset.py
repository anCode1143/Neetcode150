from typing import List

def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k != 0:
        return False
    subsetTarget = sum(nums) / k
    def canPartition(groups, index):
        if index == len(nums):
            if len(groups) != k:
                return False
            for group_sum in groups:
                if group_sum != subsetTarget:
                    return False
            return True
        for i in range(len(groups)):
            if groups[i] + nums[index] <= subsetTarget:
                groups[i] += nums[index]
                if canPartition(groups, index+1):
                    return True
                groups[i] -= nums[index]
        if len(groups) < k:
            groups.append(nums[index])
            if canPartition(groups, index+1):
                return True
            groups.pop()
    
    if canPartition([], 0): return True
    return False