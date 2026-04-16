def checkValidString(self, s: str) -> bool:
    leftMin, leftMax = 0, 0
    for char in s:
        if char == '(':
            leftMax += 1
            leftMin += 1
        elif char == ')':
            leftMax -= 1
            if leftMax < 0: return False
            leftMin = max(0, leftMin-1)
        else:
            leftMax += 1
            leftMin = max(0, leftMin-1)
            
    if leftMin == 0:
        return True
    else:
        return False