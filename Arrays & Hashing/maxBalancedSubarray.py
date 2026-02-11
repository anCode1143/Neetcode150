from typing import List
def longestBalanced(self, nums: List[int]) -> int:
    answer = 0
    for left in range(len(nums)):
        odd = set()
        even = set()
        for right in range(left, len(nums)):
            if nums[right] % 2 == 0:
                even.add(nums[right])
            if len(odd) == len(even):
                answer = max(answer, right - left + 1)
    return answer