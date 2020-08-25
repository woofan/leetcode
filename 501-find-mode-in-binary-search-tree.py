# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        tree_ele = []
        def myhelp(root):
            if not root:
                return
            if root.left:
                myhelp(root.left)
            if root.right:
                myhelp(root.right)
            tree_ele.append(root.val)
            return
        myhelp(root)
        p = collections.Counter(tree_ele).most_common(1)[0][1]
        temp = {}
        for i in tree_ele:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i,j in temp.items():
            if j == p:
                res.append(i)
        return res