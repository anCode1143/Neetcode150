from typing import List
def findTargetSumWays(nums: List[int], target: int) -> int:
    # init topMap and bottomMap, topMap[0] = 1
    # nested for loop, upper iterates len(nums) times, inner iterates through topmap keys, updating bottommap
    # exit inner loop, topmap = bottompmap.copy() 
    # exit outer loop, return bottom[target]
    bottomMap = {}
    topMap = {}
    topMap[0] = 1
    for numsElement in nums: # 2
        for key in topMap: # 0
            if (key - numsElement) in bottomMap:
                bottomMap[key - numsElement] += topMap[key]
            else:
                bottomMap[key - numsElement] = topMap[key]
            if (key + numsElement) in bottomMap:
                bottomMap[key + numsElement] += topMap[key]
            else:
                bottomMap[key + numsElement] = topMap[key]
        topMap = bottomMap.copy()
        bottomMap = {}
    return topMap[target] if target in topMap else 0