def tribonacci(self, n: int) -> int:
    index1 = 0
    index2 = 1
    index3 = 1
    if n == 0:
        return 0
    if n < 3:
        return 1
    for current in range(3, n+1):
        current = index1 + index2 + index3
        index1 = index2
        index2 = index3
        index3 = current
    return index3

"""
cue for diagnosing pattern - tracking future value with past one

how to implement the solution
    init first three values
    iterate till target; calculate new value and shift all variables forward

struggled parts
    shifting elements for constant space complexity

complexity details
    speed - linear, goes up to the target from 0
    memory - constant, only tracking n-3 values
"""