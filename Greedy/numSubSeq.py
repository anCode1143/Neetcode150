def numOfSubsequences(s: str) -> int:
    # count if L is at front
    # count if T at end
    # find optimal C position by keping track of Ls and Ts
        # increment Ls and decrement Ts
    tAmount = s.count("T")
    optimalC = [0, 0]
    currLs = 0
    currTs = tAmount
    for index in range(len(s)):
        if s[index] == "L":
            currLs += 1
        if optimalC[1] < currLs*currTs:
            optimalC[0] = index+1
            optimalC[1] = currLs*currTs
        if s[index] == "T":
            currTs -= 1

    def LCTSubsequences(string):
        l = 0
        lc = 0
        lct = 0
        for char in string:
            if char == 'L':
                l += 1
            if char == "C":
                lc += l
            if char == "T":
                lct += lc
        return lct
    
    appendL = LCTSubsequences("L"+s)
    appendT = LCTSubsequences(s+"T")
    appendC = LCTSubsequences(s[:optimalC[0]] + "C" + s[optimalC[0]:])
    return max(appendL, appendC, appendT)

print(numOfSubsequences("LTBLLTTALT"))

"""
cue for diagnosing pattern - understand you need to count substrings and then interpret the best positions, how to do these things in minimal complexity

how to implement the solution - 
    iterate the string finding the optimal C position in linear time
    implement a substring count method of linear time
    compare counts among optimal L, C, and T insertions

struggled parts - optimal string traversal in finding substring

complexity details
        speed - linear, iterate the string once to find the optimal C position
        space - constant 
"""