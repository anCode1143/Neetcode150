from typing import List


def calPoints(operations: List[str]) -> int:
    pointStack = []
    for operation in operations:
        if operation == 'D':
            pointStack.append(pointStack[-1]*2)
        elif operation == 'C':
            pointStack.pop()
        elif operation == '+':
            pointStack.append(pointStack[-1]+pointStack[-2])
        else:
            pointStack.append(int(operation))
    return sum(pointStack)

print(calPoints(["5","2","C","D","+"]))