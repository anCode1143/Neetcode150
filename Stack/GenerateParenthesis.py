def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    valid = []
    answer = []

    def backtrack(open, close):
        if open == close == n:
            answer.append("".join(valid))
            return
        
        if open < n:
            valid.append("(")
            backtrack(open+1, close)
            valid.pop()

        if open > close:
            valid.append(")")
            backtrack(open, close+1)
            valid.pop()

        return answer
            
    return backtrack(0, 0)

print(generateParenthesis(3))