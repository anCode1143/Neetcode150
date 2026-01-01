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