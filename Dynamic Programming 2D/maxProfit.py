from typing import List
def maxProfit(self, prices: List[int]) -> int:
    dp = {}

    def dfs(index, buying):
        if index >= len(prices):
            return 0
        if (index, buying) in dp:
            return dp[index, buying]
        
        cooldown = dfs(index+1, buying)
        if buying:
            value = dfs(index +1, not buying) - prices[index]
        else:
            value = dfs(index +2, not buying) + prices[index]
        dp[index, buying] = max(cooldown, value)
        return max(cooldown, value)
    
    return dfs(0, True)