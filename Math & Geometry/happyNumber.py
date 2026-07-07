def isHappy(n: int) -> bool:
    seen = set()
    while n not in seen:
        seen.add(n)
        new = 0
        for digit in str(n):
            new += int(digit) ** 2
        n = new
        if n == 1:
            return True
    return False

print(isHappy(19))