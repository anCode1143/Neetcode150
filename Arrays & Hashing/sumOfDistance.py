from collections import defaultdict
from typing import List

def distance(self, nums: List[int]) -> List[int]:
    valueToIndices = defaultdict(list)
    for index, value in enumerate(nums):
        valueToIndices[value].append(index)

    answer = [0] * (len(nums) - 1)
    for groupKey in valueToIndices.keys():
        localSum = sum(valueToIndices[groupKey])
        prefixSum = 0
        for elementIndex, originalIndex in enumerate(valueToIndices[groupKey]):
            left = elementIndex * originalIndex - prefixSum
            rightCount = len(valueToIndices[groupKey]) - elementIndex - 1
            right = (localSum - prefixSum - valueToIndices[groupKey][elementIndex]) - rightCount * originalIndex
            answer[originalIndex] = left + right
    return answer