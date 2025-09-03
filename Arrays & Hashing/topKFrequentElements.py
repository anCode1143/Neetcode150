def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    cardinal_map = {}
    for element in nums:
        if not element in cardinal_map:
            cardinal_map[element] = 1
        else:
            cardinal_map[element] += 1
    answer = [label for label, value in sorted(cardinal_map.items(), key= lambda item:item[1], reverse=True)][:k]
    return answer

input = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(topKFrequent(input, 2))