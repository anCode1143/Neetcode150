from typing import List


def sortColors(nums: List[int]) -> None:
    colourCount = {}
    colourCount[0] = 0
    colourCount[1] = 0
    colourCount[2] = 0
    for number in nums:
        colourCount[number] += 1
    index = 0
    for colour in range(3):
        for _ in range(colourCount[colour]):
            nums[index] = colour
            index += 1

colours = [2,0,2,1,1,0]
sortColors(colours)
print(colours)