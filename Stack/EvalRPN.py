import operator
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b) 
    }

    stack = []
    for element in tokens:
        try:
            stack.append(int(element))
        except ValueError:
            numA = stack.pop()
            numB = stack.pop()
            ans = ops[element](numB, numA)
            stack.append(ans)
    return stack.pop()
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))   