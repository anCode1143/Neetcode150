from typing import List

def mostPoints(self, questions: List[List[int]]) -> int:
    if len(questions) == 1: return questions[0][0]
    dp = [0] * len(questions)
    dp[-1] = questions[-1][0]
    for dpIndex in range(len(questions)-2, -1, -1):
        dp[dpIndex] = max(dp[dpIndex+1], 
                        questions[dpIndex][0] + (dp[questions[dpIndex][1] + 1 + dpIndex]
                            if questions[dpIndex][1] + 1 + dpIndex < len(dp) else 0))
    return max(dp[0], dp[1])