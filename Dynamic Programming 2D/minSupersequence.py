def shortestCommonSupersequence(str1: str, str2: str) -> str:
    dp = [[""] * len(str1) for _ in range(len(str2))]
    if str1[0] == str2[0]:
        dp[0][0] = str2[0]
    for col in range(1, len(str1)):
        if dp[0][col-1] != "":
            dp[0][col] = dp[0][col-1]
        elif str1[col] == str2[0]:
            dp[0][col] = str1[col]
    for row in range(1, len(str2)):
        if dp[row-1][0] != "":
            dp[row][0] = dp[row-1][0]
        elif str2[row] == str1[0]:
            dp[row][0] = str2[row]
    for row in range(1, len(str2)):
        for col in range(1, len(str1)):
            if str2[row] == str1[col]:
                dp[row][col] = dp[row-1][col-1] + str1[col]
            else:
                if len(dp[row-1][col]) > len(dp[row][col-1]):
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row][col-1]
    
    lcs = dp[-1][-1]
    answer = []
    str1Pointer, str2Pointer, lcsPointer = 0, 0, 0
    while lcsPointer < len(lcs):
        if str1Pointer >= len(str1):
            answer.append(str2[str2Pointer:])
            return ''.join(answer)
        if str2Pointer >= len(str2):
            answer.append(str1[str1Pointer:])
            return ''.join(answer)
        while str1Pointer < len(str1) and str1[str1Pointer] != lcs[lcsPointer]:
            answer.append(str1[str1Pointer])
            str1Pointer += 1
        while str2Pointer < len(str2) and str2[str2Pointer] != lcs[lcsPointer]:
            answer.append(str2[str2Pointer])
            str2Pointer += 1
        answer.append(lcs[lcsPointer])
        lcsPointer += 1
        str1Pointer += 1
        str2Pointer += 1
    answer.append(str2[str2Pointer:])
    answer.append(str1[str1Pointer:])
    return ''.join(answer)

print(shortestCommonSupersequence("abac", "cab"))