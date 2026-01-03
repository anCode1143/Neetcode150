from typing import List
def minCostClimbingStairs(self, cost: List[int]) -> int:
    a = cost[0]
    b = cost[1]
    for stepIndex in range(2, len(cost)):
        new = cost[stepIndex] + min(a, b)
        a = b
        b = new
    return min(a, b)

"""
cue for diagnosing pattern - tracking future value with past one

how to implement the solution
    init first two values
    iterate till target; calculate new value and shift all variables forward

struggled parts
    shifting elements for constant space complexity

complexity details
    speed - linear, goes up to the target from 0
    memory - constant, only tracking n-2 values
"""