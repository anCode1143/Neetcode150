from collections import defaultdict
from typing import List
def findJudge(n: int, trust: List[List[int]]) -> int:
    trustsKey = defaultdict(list)
    keyTrusts = defaultdict(list)
    for a, b in trust:
        trustsKey[b].append(a)
        keyTrusts[a].append(b)

    judge = None
    for number in range(1, n):
        if not keyTrusts[number] and len(trustsKey[number]) == n - 1:
            if judge == None:
                judge = number
            else:
                return -1
    return judge if isinstance(judge, int) else -1

print(findJudge(3, [[1,3],[2,3]]))