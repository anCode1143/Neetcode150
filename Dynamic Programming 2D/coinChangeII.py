from typing import List
def change(amount: int, coins: List[int]) -> int:
    bottom = [0] * (amount + 1)
    bottom[0] = 1
    top = bottom.copy()
    for row in range(len(coins)):
        for index in range(amount+1):
            top[index] = bottom[index] + (top[index - coins[row]] if index - coins[row] >= 0 else 0)
        bottom = top.copy()
        top = [0] * (amount + 1)
        top[0] = 1
    return bottom[amount]


print(change(5, [1, 2, 5]))