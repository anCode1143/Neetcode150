from collections import defaultdict
from typing import List

def totalFruit(fruits: List[int]) -> int:
    if len(fruits) == 1:
        return 1
    fruitTypes = defaultdict(int)
    fruitTypes[fruits[0]] += 1
    fruitTypes[fruits[1]] += 1
    left, right = 0, 1
    answer = 2
    while right < len(fruits)-1:
        right += 1
        fruitTypes[fruits[right]] += 1
        while len(fruitTypes) > 2:
            fruitTypes[fruits[left]] -= 1
            if fruitTypes[fruits[left]] == 0:
                del fruitTypes[fruits[left]]
            left += 1
        answer = max(answer, right - left + 1)
    return answer

print(totalFruit([1,2,1]))