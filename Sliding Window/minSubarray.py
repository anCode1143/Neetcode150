def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    curr = nums[0]
    answer = float('inf')
    left, right = 0, 0
    while right < len(nums):
        if curr >= target:
            answer = min(answer, right - left + 1)
            curr -= nums[left]
            left += 1
        else: # curr < target
            right += 1
            curr += nums[right] if right < len(nums) else 0
        if left > right:
            right += 1
            curr += nums[right] if right < len(nums) else 0
    return answer if not answer == float('inf') else 0