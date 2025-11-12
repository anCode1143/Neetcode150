def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    # [1,2,3,1]
    for price in nums:
        temp = max(rob1 + price, rob2)
        rob1 = rob2
        rob2 = temp
    return rob1
        
        

        