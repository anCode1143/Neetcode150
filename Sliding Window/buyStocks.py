from typing import List
def maxProfit(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0
    buy, sell = 0, 1
    profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = max(profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))