def minDistance(word1: str, word2: str) -> int:
    # init bottom len(w2) to 0
    # for row from last value of w1
        # init top, top[len(w2)] = row
        # iterate currIndex from second last value of top
            # find rightVal = top[currIndex -1]+1, bottomVal = bottom[currIndex]+1, diagonal = bottom[currIndex+1]+1
            # if w1[row] == w2[currIndex]: diagonal -= 1
            # top[currIndex] = max(bottom, top, diagonal)
        # bottom = top.copy()
    # return bottom[0]

    bottom = list(range(len(word2), -1, -1))
    rightMostVal = 0
    for row in range(len(word1)-1, -1, -1):
        top = [-1] * (len(word2)+1)
        rightMostVal += 1
        top[-1] = rightMostVal
        for currIndex in range(len(word2)-1, -1, -1):
            rightVal = top[currIndex+1]+1
            bottomVal = bottom[currIndex]+1
            if word1[row] == word2[currIndex]:
                diagonal = bottom[currIndex+1]
            else:
                diagonal = bottom[currIndex+1] + 1
            top[currIndex] = min(bottomVal, rightVal, diagonal)
        bottom = top.copy()
    return bottom[0]

print(minDistance("abd", "acd"))