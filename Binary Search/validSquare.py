def isPerfectSquare(num: int) -> bool:
    left = 1
    right = num
    middle = ((right - left) // 2) + left
    while left <= right:
        if middle ** 2 > num:
            right = middle - 1
        elif middle ** 2 < num:
            left = middle + 1
        else:
            return True
        middle = ((right - left) // 2) + left
    return False