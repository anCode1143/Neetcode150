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

"""
cue for diagnosing pattern - parentheses validity can utilise stacks well

how to implement the solution
    iterate through string with a map and stack
            for stack: if open, add index, if close, pop index. if stack empty and close, add to remove
            add every element to map as index:char pair
        add stack remainder to remove
        use remainder array to remove values from map
        rebuild string with updated map

struggled parts
    overcoming expensive char deletion operation for strings

complexity details
    speed - linear, iterates through string, merges stack, iterate remove, build string
    memory - linear, creates stack and remove, and a map, and new string, all linear
"""