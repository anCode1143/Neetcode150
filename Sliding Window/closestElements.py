from typing import List
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    if len(arr) < 2 or k == len(arr):
        return arr
    left, right = 0, len(arr) - 1
    while right - left >= k:
        if abs(arr[left]-x) > abs(arr[right]-x):
            left += 1
        else:
            right -= 1
    return arr[left:right+1]

print(findClosestElements([1,1,2,3,4,5], 4, -1))