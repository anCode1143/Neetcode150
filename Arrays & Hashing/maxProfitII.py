def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    position = prices[0]
    for price in prices:
        if position > price:
            position = price
        elif position < price:
            answer += price - position
            position = price
    return answer