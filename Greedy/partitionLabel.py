from typing import List

def partitionLabels(s: str) -> List[int]:
    # create a dict of chars to a list of each appearance in s as an index
    charToInstances = {}
    for charIndex in range(len(s)):
        if s[charIndex] in charToInstances:
            charToInstances[s[charIndex]].append(charIndex)
        else:
            charToInstances[s[charIndex]] = [charIndex]

    partitionIndex = 0
    answer = []
    while charToInstances:
        partitionEnd = charToInstances[s[partitionIndex]][-1]
        inPartition = set()
        index = partitionIndex
        while index <= partitionEnd:
            if s[index] not in inPartition:
                inPartition.add(s[index])
                partitionEnd = max(partitionEnd, charToInstances[s[index]][-1])
            index += 1
        answer.append(partitionEnd - partitionIndex + 1)
        for char in inPartition:
            del charToInstances[char]
        partitionIndex = index
    return answer


print(partitionLabels("ababcc"))