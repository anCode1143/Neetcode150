def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    def collision(asteroid):
        if not stack:
            stack.append(asteroid)
        elif asteroid == stack[-1]:
            stack.pop()
        elif stack[-1] < abs(asteroid):
            stack.pop()
            collision(asteroid)
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            collision(asteroid)
    return stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack