def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # init bottom, bottom[-1] = True then iterate backwards from the rest
        # if bottom[index+1] == True and s3[len(s2)+index] = s2[index], bottom[index] = True
    # top = [] * (len(s1) + 1)
    # for row in range(len(s2), -1, -1)
        # for arrIndex in range(len(s1)+1, -1, -1)
            # if top[index+1] == True and s3[len(s1)+index] = s1[index], top[index] = True or
            # if bottom[index] == True and s3[len(s2)+index] = s2[index], top[index] = True
        # bottom = top, clear top
    # return bottom[0]
    if len(s1) + len(s2) != len(s3):
        return False

    bottom = [False] * (len(s1)+1)
    bottom[-1] = True
    for index in range(len(bottom)-2, -1, -1):
        if bottom[index+1] == True and s3[len(s2)+index] == s1[index]:
            bottom[index] = True
    top = [False] * (len(s1)+1)
    for row in range(len(s2)-1, -1, -1):
        for arrIndex in range(len(s1), -1, -1):
            if arrIndex < len(top)-1 and top[arrIndex+1] == True and s3[row+arrIndex] == s1[arrIndex]:
                top[arrIndex] = True
            elif bottom[arrIndex] == True and s3[row+arrIndex] == s2[row]:
                top[arrIndex] = True
        bottom = top.copy()
        top = [False] * (len(s1)+1)
    return bottom[0]

print(isInterleave("ace", "bdfg", "abcdefg"))