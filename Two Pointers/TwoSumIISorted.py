def twoSum(numbers, target):
    left_index = 0
    right_index = len(numbers) - 1

    if numbers[left_index] + numbers[right_index] == target:
        return [left_index + 1, right_index + 1]
    
    while right_index >= 1:
        left_index = 0
        while left_index < right_index:
            if numbers[left_index] + numbers[right_index] == target:
                return [left_index + 1, right_index + 1]
            if numbers[left_index] + numbers[right_index] > target:
                break
            left_index += 1
        right_index -=1

numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))