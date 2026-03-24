from collections import defaultdict

def countTriples(n: int) -> int:
    squares = set()
    squares.add(1)
    squarePair = defaultdict(int)
    answer = 0
    for number in range(2, n+1):
        numSq = number**2
        for square in squares:
            squarePair[square + numSq] += 2
        squares.add(numSq)
        if numSq in squarePair:
            answer += squarePair[numSq]
    return answer

print(countTriples(25))