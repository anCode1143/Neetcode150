def plusOne(self, digits: List[int]) -> List[int]:
    if digits[-1] == 9:
        carry = True
    else:
        carry = False
        digits[-1] += 1
        return digits
    index = len(digits) - 1
    while carry:
        if index < 0:
            answer = [1]
            for digit in digits:
                answer.append(digit)
            return answer
        if digits[index] == 9:
            digits[index] = 0
            index -= 1
        else:
            digits[index] += 1
            carry = False
    return digits