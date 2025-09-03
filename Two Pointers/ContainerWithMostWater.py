def maxArea(height):
    left = 0
    right = len(height)-1
    answer = 0
    while left < right:
        intermediate = (right-left) * min(height[left], height[right])
        if intermediate > answer:
            answer = intermediate
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return answer

print(maxArea([1,1]))