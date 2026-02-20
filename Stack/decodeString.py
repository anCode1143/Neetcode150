from collections import deque
def decodeString(s: str) -> str:
    stack = []
    for char in s:
        if char == ']':
            subString = deque()
            while stack[-1].isalpha():
                subString.appendleft(stack[-1])
                stack.pop()
            stack.pop()
            number = deque()
            while stack and stack[-1].isdigit():
                number.appendleft(stack[-1])
                stack.pop()
            number = int(''.join(str(digit) for digit in number))
            subString = ''.join(subString)
            for _ in range(number):
                stack.append(subString)
        else:
            stack.append(char)
    return ''.join(stack)