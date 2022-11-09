#动态规划法，dp[i][j][k]代表矩阵[i][j]位置的k方向的最长连续1长度,k=0,1,2,3;可以简化为dp[i][j]代表四个方向中最短的距离。
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n for i in range(n)] for j in range(n)]
        mymap = set()
        for i,j in mines:
            mymap.add((i,j))
        ans = 0
        for i in range(n):
            count = 0
            for j in range(n):
                if (i,j) in mymap:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j],count)
            count = 0
            for j in range(n-1,-1,-1):
                if (i,j) in mymap:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j],count)
        for j in range(n):
            count = 0
            for i in range(n):
                if (i,j) in mymap:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j],count)
            count = 0
            for i in range(n-1,-1,-1):
                if (i,j) in mymap:
                    count = 0
                else:
                    count += 1
                dp[i][j] = min(dp[i][j],count)
        for i in range(n):
            for j in range(n):
                ans = max(ans, dp[i][j])
        return ans

#暴力搜索，超时
# class Solution:
#     def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
#         ans = 0
#         for i in range(n):
#             for j in range(n):
#                 tmp_level = 0
#                 point = 1 if [i,j] not in mines else 0
#                 if point:
#                     tmp_level = 1
#                     level = 1
#                     while i-level>=0 and i+level<n and j-level>=0 and j+level<n:
#                         flag = 0
#                         for x_tmp, y_tmp in [[-level,0],[0,level],[level,0],[0,-level]]:
#                             x = i + x_tmp
#                             y = j + y_tmp
#                             if [x,y] not in mines:
#                                 flag += 1
#                         if flag == 4:
#                             tmp_level += 1
#                             level += 1
#                         else:
#                             break
#                     ans = max(ans,tmp_level)
#         return ans