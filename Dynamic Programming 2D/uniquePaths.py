def uniquePaths(m: int, n: int) -> int:
    row = [1] * n
    for iteratingRows in range(m-1):
        newRow = [1] * n
        for cell in range(n-2, -1, -1):
            newRow[cell] = row[cell] + newRow[cell+1]
        row = newRow
    return row[0]

print(uniquePaths(3, 7))