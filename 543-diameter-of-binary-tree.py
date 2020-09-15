# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        def myhelp(root):
            if not root:
                return 0
            L = myhelp(root.left)
            R = myhelp(root.right)
            self.res = max(self.res,L+R+1)
            return max(L,R) + 1
        myhelp(root)
        return self.res - 1