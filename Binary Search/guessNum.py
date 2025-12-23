def guessNumber(self, n: int) -> int:
    if n == 1:
        return 1
    estimate = n//2
    upper = n
    lower = 1
    while not guess(estimate) == 0:
        if guess(estimate) == - 1:
            upper = estimate - 1
        if guess(estimate) == 1:
            lower = estimate + 1
        estimate = ((upper - lower) // 2) + lower
    return estimate