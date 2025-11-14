def longestPalindrome(s):
    # sbaaab
    answer = ""

    def extendPalindrome(pointerLeft, pointerRight):
        answer = ""
        while pointerLeft >= 0 and pointerRight < len(s):
            if s[pointerLeft] == s[pointerRight]:
                answer = s[pointerLeft:pointerRight+1]
                pointerLeft -= 1
                pointerRight += 1
            else:
                return answer
        return answer

    for index in range(len(s)):
        answer = max(extendPalindrome(index, index + 1), extendPalindrome(index, index), answer, key=len)
    return answer

print(longestPalindrome("babad"))