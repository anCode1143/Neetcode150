from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    # run for loops recursively appending to array builder, 
    #   calling on next recursive instance with modified lesser arr and builder
    answer = []
    def backtracking(arrBuilder, arr):
        if not arr:
            answer.append(arrBuilder.copy())
            return
        for index in range(len(arr)):
            arrBuilder.append(arr[index])
            next = arr[:index] + (arr[index+1:] if index < len(arr)-1 else [])
            backtracking(arrBuilder, next.copy())
            arrBuilder.pop()
    backtracking([], nums)
    return answer

print(permute([1, 2, 3]))
# len(nums)! * len(nums)^2