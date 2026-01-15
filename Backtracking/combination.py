from typing import List
def combine(n: int, k: int) -> List[List[int]]:
    answer = []
    def backtracking(number, path):
        if len(path) == k:
            answer.append(path)
            return
        for candidate in range(number+1, n+1):
            path.append(candidate)
            backtracking(candidate, path.copy())
            path.pop()

    backtracking(0, [])
    return answer

print(combine(3, 2))