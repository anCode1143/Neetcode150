def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    top = 0
    bottom = len(matrix) - 1
    middle = 0
    while top <= bottom:
        middle = ((bottom - top) // 2) + top
        if target > matrix[middle][0]:
            if target <= matrix[middle][-1]:
                break
            top = middle + 1
        elif target < matrix[middle][0]:
            bottom = middle - 1
        else:  # target == matrix[middle][0]
            return True
        
    left = 0
    right = len(matrix[0]) - 1
    while left <= right:
        row_middle = ((right - left) // 2) + left
        if target > matrix[middle][row_middle]:
            left = row_middle + 1
        elif target < matrix[middle][row_middle]:
            right = row_middle - 1
        else:  # target == matrix[middle][row_middle]
            return True
    return False



matrix = [
    [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ],
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
]

test = [[1]]

test2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(searchMatrix(test2, 3))