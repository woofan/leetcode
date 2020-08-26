# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree_ele = []
        def myhelp(root):
            if not root:
                return
            tree_ele.append(root.val)
            if root.left:
                myhelp(root.left)
            if root.right:
                myhelp(root.right)
        myhelp(root)
        res = float('inf')
        tree_ele = sorted(tree_ele)
        for i in range(len(tree_ele)-1):
            temp = abs(tree_ele[i+1] - tree_ele[i])
            if temp == 0:
                return 0
            if temp < res:
                res = temp
        return res