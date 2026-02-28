def getKth(lo: int, hi: int, k: int) -> int:
    powerToNum = []
    numToPower = {}
    for num in range(lo, hi+1):
        intermediaries = [num]
        power = 0
        interm = num
        while not interm == 1:
            if interm % 2 == 0:
                interm = interm // 2
            else:
                interm = (3 * interm) + 1
            intermediaries.append(interm)
            power += 1
            if interm in numToPower:
                power += numToPower[interm]
                break
        powerToNum.append([power, num])
        for interm in intermediaries:
            if interm in numToPower: break
            numToPower[interm] = power
            power -= 1
    powerToNum.sort()
    return powerToNum[k-1][1]

print(getKth(12, 15, 2))