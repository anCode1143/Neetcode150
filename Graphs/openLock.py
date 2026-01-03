from collections import deque
from typing import List

def openLock(deadends: List[str], target: str) -> int:
    visited = set(deadend for deadend in deadends)
    if "0000" in visited:
        return -1
    visited.add("0000")
    queue = deque()
    queue.append(("0000", 0))
    while queue:
        parents = len(queue)
        for _ in range(parents):
            currPos, steps = queue.popleft()
            if currPos == target:
                return steps
            for digitChange in range(4):
                if currPos[digitChange] == "9":
                    up = currPos[:digitChange] + "0" + currPos[digitChange+1:]
                else: up = currPos[:digitChange] + str(int(currPos[digitChange])+1) + currPos[digitChange+1:]
                if currPos[digitChange] == "0":
                    down = currPos[:digitChange] + "9" + currPos[digitChange+1:]
                else: down = currPos[:digitChange] + str(int(currPos[digitChange])-1) + currPos[digitChange+1:]

                if up not in visited:
                    visited.add(up)
                    queue.append((up, steps+1))
                if down not in visited:
                    visited.add(down)
                    queue.append((down, steps+1))
    return -1

print(openLock(["0201","0101","0102","1212","2002"], "0202"))
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        visit = set(deadends)
        if "0000" in visit:
            return -1

        begin = {"0000"}
        end = {target}
        steps = 0

        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin

            steps += 1
            temp = set()
            for lock in begin:
                for i in range(4):
                    for j in [-1, 1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextLock = lock[:i] + digit + lock[i+1:]

                        if nextLock in end:
                            return steps
                        if nextLock in visit:
                            continue
                        visit.add(nextLock)
                        temp.add(nextLock)
            begin = temp
        return -1
    
"""
cue for diagnosing pattern - inputs needs to be iterated incrementally, draws similarity to path finding

how to implement the solution
    put banned nodes in a set
    do bfs going 8 directions, -1 and +1 for each digit. add to visit set.
    check if current == target

struggled parts - wanted to transfer to int but ultimately had no point. 
    make sure to think things through at a high level

improvement from standard solution - bidirectional for speed optimisation

complexity details
    speed - digits^wheels, as thats the amount of nodes the algorithm will go through worst case
    memory - digits^wheels, amount of possible elements to be stored in visit
    both are technically linear
"""