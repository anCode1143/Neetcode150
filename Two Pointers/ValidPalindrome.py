def isPalindrome(s):
    string = ''.join(char for char in s.lower() if char.isalnum())
    right = len(string) - 1
    for left in range(len(string)):
        if not string[left] == string[right]:
            return False
        if (left + 2) >= right:
            return True 
        right -= 1

test = "  "
print(isPalindrome(test))