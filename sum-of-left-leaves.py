# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return self.res

        def dfs(root, flag):
            if not root:
                return
            if flag == 1 and not root.left and not root.right:
                self.res += root.val
            dfs(root.left, 1)
            dfs(root.right, 2)

        dfs(root, 2)
        return self.res