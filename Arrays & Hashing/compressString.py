from typing import List

def compress(chars: List[str]) -> int:
    ptr = 0
    replacePtr = 0
    while ptr < len(chars):
        counter = 1
        while ptr+1 < len(chars) and chars[ptr] == chars[ptr+1]:
            counter += 1
            ptr += 1
        chars[replacePtr] = chars[ptr]
        replacePtr += 1
        if counter > 1:
            for digit in str(counter):
                chars[replacePtr] = digit
                replacePtr += 1
        ptr += 1
    print(chars)
    return replacePtr

print(compress(["a","a","b","b","c","c","c"]))