import math
def isEdibleSpeed(piles, eating_speed, h):
    total_hours = 0
    for pile in piles:
        hours_for_pile = math.ceil(pile / eating_speed)
        total_hours += hours_for_pile
        
        # Early terminate
        if total_hours > h:
            return False
    
    return total_hours <= h

def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    min_eating_speed = max(piles)
    left, right = 1, min_eating_speed
    while left <= right:
        middle = ((right - left) // 2) + left
        if isEdibleSpeed(piles, middle, h):
            right = middle - 1
            min_eating_speed = middle
        else:
            left = middle + 1
    return min_eating_speed

print(minEatingSpeed([30,11,23,4,20], 6))