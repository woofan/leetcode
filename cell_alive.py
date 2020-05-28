import copy
def gameOfLife( board) :
    """
    Do not return anything, modify board in-place instead.
    """
    temp = copy.deepcopy(board)
    for i in temp:
        i.append(0)
        i.insert(0,0)
    temp.append([0]*len(temp[0]))
    temp.insert(0,[0]*len(temp[0]))
    for i in range(1,len(temp)-1):
        for j in range(1,len(temp[0])-1):
            alives = temp[i-1][j-1] + \
                     temp[i-1][j] + \
                     temp[i-1][j+1] + \
                     temp[i][j-1] + \
                     temp[i][j+1] + \
                     temp[i+1][j-1] + \
                     temp[i+1][j] + \
                     temp[i+1][j+1]
            if alives ==2 :
                board[i - 1][j - 1] = board[i-1][j-1] & 1
            elif alives == 3:
                board[i - 1][j - 1] = 1
            else:
                board[i-1][j-1] = 0
    return temp,board

