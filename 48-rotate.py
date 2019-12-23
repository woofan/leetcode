'''
题目要求顺时针旋转矩阵90度，可以分解为两步。先对矩阵做转置，再做左右对称互换。
即  1 2 3       1 4 7      7 4 1
    4 5 6  ->   2 5 8  ->  8 5 2
    7 8 9       3 6 9      9 6 3
'''
def rotate(matxir):
    l = len(matxir[0])
    x=0
    for i in range(l):
        for j in range(x,l):
            temp = matxir[i][j]
            matxir[i][j] = matxir[j][i]
            matxir[j][i] = temp
        x += 1
    half_length = l//2
    for i in range(l):
        for j in range(half_length):
            temp = matxir[i][j]
            matxir[i][j] = matxir[i][l-j-1]
            matxir[i][l-j-1] = temp
    return matxir


a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(rotate(a))