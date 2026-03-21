def simplifyPath(path: str) -> str:
    stack = []
    charIndex = 0
    while charIndex < len(path):
        if path[charIndex] == '/':
            charIndex += 1
            continue
        component_start = charIndex
        while charIndex < len(path) and path[charIndex] != '/':
            charIndex += 1
        component = path[component_start:charIndex]

        if component == "..":
            if stack:
                stack.pop()
        elif component == "." or component == "":
            continue
        else:
            stack.append(component)

    return "/" + "/".join(stack)

print(simplifyPath("/.../a/../b/c/../d/./"))
# Expected: /.../b/d