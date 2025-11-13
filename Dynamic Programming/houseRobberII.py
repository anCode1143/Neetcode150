def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    rob1, rob2, rob3 = 0, 0, 0
    for price in nums[1:]:
        temp = max(rob1 + price, rob2)
        rob1 = rob2
        rob2 = temp
    rob1 = 0
    for price in nums[:len(nums)-1]:
        temp = max(rob1 + price, rob3)
        rob1 = rob3
        rob3 = temp
    return max(rob2, rob3)

print(rob([2,7,9,3,1]))