def countPrimeSetBits(self, left: int, right: int) -> int:
    def is_prime(n):
        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True
    answer = 0
    for num in range(left, right + 1):
        ones = bin(num).count('1')
        if is_prime(ones): answer += 1
    return answer
