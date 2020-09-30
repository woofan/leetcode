def myfindDiagonalOrder(matrix):
    if len(matrix) == 0:
        return []
    res = []
    sign = 1
    max_len = max(len(matrix),len(matrix[0]))
    row_len = len(matrix)
    column_len = len(matrix[0])
    for i in range((2 * (max_len -1) ) + 1):
        pearl_list = []
        for j in range(i+1):
            if j < row_len and (i-j) < column_len:
                temp = matrix[j][i-j]
                pearl_list.append(temp)
        if sign == 1:
            pearl_list = pearl_list[::-1]
        for i in pearl_list:
            res.append(i)
        sign = -sign
    return res

def findDiagonalOrder(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_len = len(matrix)
    column_len = len(matrix[0])
    for i in range(row_len + column_len -1):
        temp = []
        x = 0 if i < column_len else (i - column_len + 1)
        y = i if i < column_len else column_len - 1
        while x < row_len and y > -1:
            temp.append(matrix[x][y])
            x += 1
            y -= 1
        if i%2 == 0:
            temp = temp[::-1]
        res.extend(temp)
    return res



a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
b = [[1,2],[3,4],[5,6],[7,8]]
print(findDiagonalOrder(a))