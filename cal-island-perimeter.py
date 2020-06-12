def islandPerimeter(grid):
    wasd = [(-1,0),(0,-1),(0,1),(1,0)]
    res = 0
    flag = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in wasd:
                index_x = i+k[0]
                index_y = j+k[1]
                if grid[i][j] == 1 and index_x >=0 and index_y >=0 and index_x <= len(grid)-1 and index_y <= len(grid[0])-1:
                    if grid[index_x][index_y] == 1:
                        flag +=1
            if grid[i][j] ==1 or flag >0:
                res += (4-flag)
            flag = 0
    return res

a = [[0,1]]
print(islandPerimeter(a))