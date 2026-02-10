from typing import List
def beautifulSubsets(nums: List[int], k: int) -> int:
    def isBeautiful(arr, candidate) -> bool:
        for element in arr:
            if abs(element - candidate) == k:
                return False
        return True
    
    answer = []
    def backtracking(index, curr):
        if index == len(nums):
            if curr:
                answer.append(curr)
            return
        if isBeautiful(curr, nums[index]):
            curr.append(nums[index])
            backtracking(index+1, curr)
            curr.pop()
        backtracking(index+1, curr)
    backtracking(0, [])
    return len(answer)

print(beautifulSubsets([2,4,6], 2))