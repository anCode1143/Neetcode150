def ContainsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    nums_sorted = sorted(nums)
    for index in range(len(nums_sorted) - 1):
        if (index != len(nums_sorted) - 1):
            if (nums_sorted[index] == nums_sorted[index+1]):
                return True
    return False


test_cases = [
    ([1, 2, 3, 4, 5], False),
    ([1, 2, 3, 4, 1], True),
    ([1, 1, 1, 1], True),
    ([], False),
    ([0], False),
    ([-1, -2, -3, -1], True),
]

for i, (nums, expected) in enumerate(test_cases):
    result = ContainsDuplicate(nums)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")