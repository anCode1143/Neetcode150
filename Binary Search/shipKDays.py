from typing import List
def shipWithinDays(weights: List[int], days: int) -> int:
    def canShip(capacity):
        load = 0
        index = 0
        for _ in range(days):
            load = 0
            while index < len(weights) and load + weights[index] <= capacity:
                load += weights[index]
                index += 1
        if index == len(weights):
            return True
        else: 
            return False
            
    curr = high = sum(weights)
    low = 1
    while low <= high:
        guess = ((high - low)//2)+low
        if canShip(guess):
            curr = guess
            high = guess - 1
        else:
            low = guess + 1
    return curr

print(shipWithinDays([1,2,3,1,1], 4))
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res
    
"""
cue for diagnosing pattern - finding the optimised value by a series of guesses

how to implement the solution
    set low as 1 and high as the sum of the array
    do binary search with a helper function verifying if the guess is valid

struggled parts - 
    helper function read, the question
    careful of borders in binary search

complexity details
    speed - nlogn, binary search is logn * verifying the guess each time is n
    memory - constant
"""