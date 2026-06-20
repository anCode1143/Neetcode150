def mySqrt(x: int) -> int:
    left, right = 0, x
    middle = 0
    while left <= right:
        middle = int((right - left)/2)+left
        guess = middle * middle
        if guess == x:
            return int(middle)
        if guess > x:
            right = middle - 1
        if guess < x:
            left = middle + 1
    return int(middle)

print(mySqrt(3))