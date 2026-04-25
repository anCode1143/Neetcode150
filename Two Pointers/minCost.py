from typing import List

def minCost(colors: str, neededTime: List[int]) -> int:
    if len(colors) < 2:
        return 0
    left, right = 0, 1
    answer = 0
    while right < len(colors):
        if colors[left] != colors[right]:
            left = right
            right += 1
        else:
            if neededTime[left] < neededTime[right]:
                answer += neededTime[left]
                left = right
                right += 1
            else:
                answer += neededTime[right]
                right += 1
    return answer

print(minCost("aabaa", [1,2,3,4,1]))