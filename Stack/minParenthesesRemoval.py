def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    toRemove = []
    sMap = {}
    for index in range(len(s)):
        sMap[index] = s[index]
        if s[index] == "(":
            stack.append(index)
        if s[index] == ")":
            if stack:
                stack.pop()
            else:
                toRemove.append(index)
    toRemove += stack
    for index in toRemove:
        sMap[index] = None
    answer = ""
    for index in range(len(s)):
        if sMap[index]: 
            answer += sMap[index]
    return answer