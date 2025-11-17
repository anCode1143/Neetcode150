def countSubstrings(s: str) -> int:
    answer = 0
    def expandPalindrome(startLeft, startRight):
        nonlocal answer
        left, right = startLeft-1, startRight+1
        answer += 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]: 
                answer += 1
                left -= 1
                right += 1
            else:
                break
            
    if not s:
        return 1
    for index in range(len(s)):
        expandPalindrome(index, index)
        if index < len(s)-1 and s[index] == s[index+1]:
            expandPalindrome(index, index+1)
    return answer

print(countSubstrings("aaa"))