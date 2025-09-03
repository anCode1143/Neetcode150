def longestConsecutive(self, nums):
    num_set = set(nums)
    longest = 0
    for number in num_set:
        length = 1
        if not (number - 1) in num_set:
            while (number + length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest