# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs_string(node,s):
            if not node:
                return s
            temp = ' '+str(node.val)+ ' '
            s.append(temp)
            if node.left:
                dfs_string(node.left,s)
            else:
                s.append('left_none')
            if node.right:
                dfs_string(node.right,s)
            else:
                s.append('right_none')
            return s
        s_string = ','.join(dfs_string(s,[]))
        t_string = ','.join(dfs_string(t,[]))
        return t_string in s_string