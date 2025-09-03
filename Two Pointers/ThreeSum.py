def threeSum(nums):
    answer = []
    nums.sort()
    a = 0
    prev_a = nums[a]
    left = a + 1
    right = len(nums) - 1
    while a < right:
        left = a + 1
        right = len(nums) - 1
        while left < right:
            if nums[a] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[a] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[a] + nums[left] + nums[right] == 0:
                answer.append([nums[a], nums[left], nums[right]])
                left += 1
                right -= 1
        a += 1
        while nums[a] == prev_a and not a == len(nums) - 1:
            a += 1
    
    seen = set()
    unique_arrays = []

    for sub in answer:
        sorted_tuple = tuple(sorted(sub))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            unique_arrays.append(sub)
    return unique_arrays

print(threeSum([-2,0,0,0,0,0,0,1,1,1,1,1,2]))