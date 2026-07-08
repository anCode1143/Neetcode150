from collections import defaultdict
from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    answer = 1
    peoplePtrL = 0
    peoplePtrR = len(people) - 1
    people.sort()
    while peoplePtrL <= peoplePtrR:
        answer += 1
        if people[peoplePtrL] + people[peoplePtrR] <= limit:
            peoplePtrL += 1
        peoplePtrR -= 1

    return answer

print(numRescueBoats([2,1], 3))