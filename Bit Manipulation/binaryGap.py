from collections import deque
def binaryGap(n: int) -> int:
    twoBits = deque([None] * 2, maxlen=2)
    answer = 0
    for bit in range(n.bit_length()):
        if (n >> bit) & 1:
            twoBits.append(bit) # type: ignore
            if not twoBits[0] == None:
                answer = max(answer, twoBits[1] - twoBits[0])
    return answer

print(binaryGap(8))