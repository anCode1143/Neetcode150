def canPartition(self, nums: List[int]) -> bool:
    target = sum(nums)/2
    if not target % 1 == 0 or len(nums) < 2:
        return False
    sums = set()
    for number in nums:
        sumsIterable = sums.copy()
        for sumsElement in sumsIterable:
            sums.add(sumsElement+number)
        if target in sums:
            return True
        sums.add(number)
    return False