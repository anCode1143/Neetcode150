from typing import List

def countCoveredBuildings(n: int, buildings: List[List[int]]) -> int:
    rowList = {row: [] for row in range(n+1)}
    buildings.sort()
    for x, y in buildings:
        rowList[y].append(x)
    sided = set()
    for y, xs in rowList.items():
        if len(xs) > 2:
            for x in xs[1:-1]:
                sided.add((x, y))
    
    colList = {col: [] for col in range(n+1)}
    buildings.sort(key = lambda key: key[1])
    for x, y in buildings:
        colList[x].append(y)
    sandwiched = set()
    for x, ys in colList.items():
        if len(ys) > 2:
            for y in ys[1:-1]:
                sandwiched.add((x, y))
    
    return len(sided & sandwiched)

print(countCoveredBuildings(3, [[1,2],[2,1],[3,1],[1,1],[2,3],[1,3]]))