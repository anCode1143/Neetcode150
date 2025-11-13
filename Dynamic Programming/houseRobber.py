def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    for price in nums:
        temp = max(rob1 + price, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
        
        

        