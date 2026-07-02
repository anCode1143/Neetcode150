from typing import List

def partition(s: str) -> List[List[str]]:
    def isPalindrome(string):
        left, right = 0, len(string)-1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
    
    answer = []
    def backtrack(path, sIndex):
        if sIndex == len(s):
            for partition in path:
                if not isPalindrome(partition):
                    return
            answer.append(path.copy())
            return
        path.append(s[sIndex])
        backtrack(path.copy(), sIndex+1)
        path.pop()
        if path:
            path[-1] += s[sIndex]
            backtrack(path.copy(), sIndex+1)
            path.pop()
    backtrack([], 0)
    return answer

print(partition('aab'))