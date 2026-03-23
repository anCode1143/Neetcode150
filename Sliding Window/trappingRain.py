from typing import List

def trap(height: List[int]) -> int:
    if not height: return 0

    left, right = 1, len(height) - 2
    maxLeft, maxRight = height[0], height[-1]
    water = 0
    while left <= right:
        if maxRight > maxLeft:
            waterHeld = maxLeft - height[left]
            water += waterHeld if waterHeld > 0 else 0
            maxLeft = max(maxLeft, height[left])
            left += 1
        else:
            waterHeld = maxRight - height[right]
            water += waterHeld if waterHeld > 0 else 0
            maxRight = max(maxRight, height[right])
            right -= 1
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2]))
#           0,1,2,3,4,5,6,7,8,9,10