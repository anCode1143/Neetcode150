from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    answer = []
    nums.sort()
    def backTracking(index, currPath):
        if index == len(nums):
            answer.append(currPath)
            return
        currPath.append(nums[index])
        backTracking(index+1, currPath[:])
        currPath.pop()
        while index < len(nums)-1 and nums[index+1] == nums[index]:
            index += 1
        backTracking(index+1, currPath[:])

    backTracking(0, [])
    return answer

print(subsetsWithDup([1, 2, 2, 3]))

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res