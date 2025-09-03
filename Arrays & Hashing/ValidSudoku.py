def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for rows in board:
        answer = noDuplicates(rows)
        if not answer:
            return False
    #columns
    for index in range(9):
        column = []
        for list in board:
            column.append(list[index])
        if not noDuplicates(column):
            return False
    #grid
    offset_x = 0
    offset_y = 0
    while not (offset_x == 9):
        grid = []
        for x in range(3):
            for y in range(3):
                grid.append(board[offset_x+x][offset_y+y])
        if not noDuplicates(grid):
            return False
        if not offset_y >= 6:
            offset_y += 3
        else:
            offset_y = 0
            offset_x += 3
    return True

def noDuplicates(test):
    clean_list = [element for element in test if element != "."]
    return len(clean_list) == len(set(clean_list))

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))