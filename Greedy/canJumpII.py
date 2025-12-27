from typing import List
def jump(nums: List[int]) -> int:
    # maxJump = nums[0], startsection = 0, steps = 1
    # while maxJump < len(nums)-1
        # for loop going through elements between startsection and maxJump, finding the next maxJump
    # return steps 
    maxJump = nums[0]
    startSection = 0
    steps = 0
    while maxJump < len(nums)-1:
        steps += 1
        prevMaxJump = maxJump
        for index in range(startSection, maxJump+1):
            maxJump = max(maxJump, nums[index]+index)
        startSection = prevMaxJump
    return steps

    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
"""
cue for diagnosing pattern - trying to find linear solution in dp-esque problem

how to implement the solution - get the max jump in each step with an idea like BFS

struggled parts - updating variables

complexity details
    speed - linear, iterates the array once
    memory - o(1)
"""