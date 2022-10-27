# coding:utf-8
# !python3
import math
import collections
import copy
import random

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def helper(g, x, y, island):#递归地找出一个岛的全部下标
            n = len(g)
            g[x][y] = 2
            island.append([x,y])
            for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if 0 <= i < n and 0<= j < n and g[i][j] == 1:
                    helper(g, i, j, island)

        #求出遇到的第一个岛的所有下标，存入island数组，然后结束循环
        n = len(grid)
        island = []
        for i in range(n):
            if not island:
                for j in range(n):
                    if grid[i][j] == 1:
                        helper(grid, i, j, island)
                        break
            else:
                break

        #通过外扩的方式（BFS）计算两岛的最近距离
        distance = 0
        p = copy.deepcopy(island)
        while True:
            tmp = []
            for x,y in p:
                for i,j in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                    if 0<= i < n and 0<=j < n:
                        if grid[i][j] == 1:
                            return distance
                        elif grid[i][j] != 2:
                            tmp.append([i,j])
                            grid[i][j] = 2
            p = tmp
            distance += 1

#初始解法，求出两个岛的所有下标island1和island2，然后求出两个下标数组中横坐标与纵坐标差的绝对值之和的最小值min_distance，结果就是min_distance-1
# class Solution:
#     def shortestBridge(self, grid: List[List[int]]) -> int:
#         def helper(g, x, y, island):#递归地找出一个岛的全部下标
#             n = len(g)
#             g[x][y] = 2
#             island.append([x,y])
#             direction = [[-1,0],[0,-1],[0,1],[1,0]]#上下左右
#             for i,j in direction:
#                 if x + i >= 0 and y+j >=0 and x+i < n and y+j < n and g[x+i][y+j]==1:
#                     helper(g, x+i, y+j, island)

#         n = len(grid)
#         island1 = []
#         island2 = []
#         min_distance = inf
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     if not island1:
#                         helper(grid, i, j, island1)
#                     else:
#                         helper(grid, i, j, island2)
#         for x,y in island1:
#             for i,j in island2:
#                 min_distance = min(min_distance,(abs(x-i)+abs(y-j)))
#         return min_distance-1
