from typing import List

def singleNumber(self, nums: List[int]) -> int:
    answer = nums[0]
    for num in nums[1:]:
        answer ^= num
    return answer