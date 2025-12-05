from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    answer = []
    def dfs(subset, index):
        if index == len(nums):
            answer.append(subset)
            return subset
        else:
            dfs(subset[:], index+1)
            subset.append(nums[index])
            dfs(subset[:], index+1)
    dfs([], 0)
    return answer

print(subsets([1, 2, 3]))