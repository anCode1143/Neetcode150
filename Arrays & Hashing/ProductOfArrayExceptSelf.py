def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = []
    prefix = []
    postfix = []
    product = 1
    for index in nums:
        product *= index
        prefix.append(product)
    product = 1
    for element in reversed((nums)):
        product *= element
        postfix.append(product)
    postfix.reverse()
    for number in range(len(nums)):
        if number == 0:
            answer.append(postfix[1])
        elif number == len(nums) - 1:
            answer.append(prefix[len(prefix)-2])
        else: answer.append(prefix[number-1]*postfix[number+1])
    return answer

print(productExceptSelf([1, 2, 3, 4]))              # Expected: [24, 12, 8, 6]
print(productExceptSelf([0, 1, 2, 3]))              # Expected: [6, 0, 0, 0]
print(productExceptSelf([2, 3, 4, 5]))              # Expected: [60, 40, 30, 24]
print(productExceptSelf([1, 0, 0, 4]))              # Expected: [0, 0, 0, 0]
print(productExceptSelf([5, 1, 10, 1]))             # Expected: [10, 50, 5, 50]
print(productExceptSelf([3, 3, 3]))                 # Expected: [9, 9, 9]
print(productExceptSelf([1, 2]))                    # Expected: [2, 1]