from math import gcd
from typing import List

def minimumTime(d: List[int], r: List[int]) -> int:
    def validT(time):
        lcm = (r[0] * r[1]) // gcd(r[0], r[1])
        s0 = time - time // r[0]           # free hours for drone 0
        s1 = time - time // r[1]           # free hours for drone 1
        usable = time - time // lcm        # hours where at least one drone is free
        return s0 >= d[0] and s1 >= d[1] and usable >= d[0] + d[1]
    
    low = 0
    high = 2 * sum(d)
    answer = high
    while low <= high:
        mid = ((high - low) // 2) + low
        if validT(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

print(minimumTime([1, 3], [2, 2]))