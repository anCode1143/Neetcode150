from typing import List
def letterCombinations(digits: str) -> List[str]:
    answer = []
    numToLetter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    def backtracking(index, curr):
        if index == len(digits):
            answer.append(curr)
            return
        for char in numToLetter[digits[index]]:
            curr += char
            backtracking(index+1, curr[:])
            curr = curr[:-1]
    backtracking(0, "")
    return answer

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res
    
"""
cue for diagnosing pattern - running every single possible combination

how to implement the solution
    init a dictionary for each number and strings
    create backtracking algorithm where backtracking is called for every possible letter

complexity details
    speed - amount of letters^len(n) * n, how much possible combinations exist times popping the last char
    memory - amount of letters^len(n) * n, amount of answers x len of answer
"""
