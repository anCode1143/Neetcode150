from typing import List
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []

    def recursion(candidates, target, current):
        if sum(current) > target:
            return
        if sum(current) == target:
            answer.append(current[:])
            return
        if candidates:
            recursion(candidates, target, current + [candidates[0]])
            recursion(candidates[1:], target, current)
        return

    recursion(candidates, target, [])
    return answer