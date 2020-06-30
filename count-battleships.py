class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                up = 0
                left = 0
                up_row = i-1
                up_column = j
                left_row = i
                left_column = j-1
                if up_row >= 0:
                    up = 1 if (board[up_row][up_column] == '.') else 0
                else:
                    up = 1
                if left_column >= 0:
                    left = 1 if (board[left_row][left_column] == '.') else 0
                else:
                    left = 1
                if board[i][j]=='X' and up ==1 and left == 1:
                    res += 1
        return res