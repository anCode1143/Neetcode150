from collections import defaultdict
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    answer = 0
    valueCount = defaultdict(int)
    valueCount[0] = 1
    currCount = 0
    for num in nums:
        currCount += num
        answer += valueCount[currCount - k]
        valueCount[currCount] += 1
    return answer

print(subarraySum([1, 2, 3], 3))

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res