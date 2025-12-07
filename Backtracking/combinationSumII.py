from typing import List
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    candidates.sort()
    def backtrack(index, selection, currentSum):
       if currentSum == target:
           answer.append(selection.copy())
           return
       if currentSum > target or index == len(candidates):
           return
       
       selection.append(candidates[index])
       backtrack(index+1, selection, currentSum + candidates[index])
       selection.pop()
       while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
           index += 1
       backtrack(index+1, selection, currentSum)

    backtrack(0, [], 0)
    
    return answer

print(combinationSum2([10,1,2,7,6,1,5], 8))