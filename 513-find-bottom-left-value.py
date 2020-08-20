# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        mylist = [root]
        res = []
        level = 0
        while len(mylist) > 0:
            level_list = []
            level += 1
            for i in range(len(mylist)):
                temp_node = mylist.pop(0)
                level_list.append(temp_node.val)
                if temp_node.left:
                    mylist.append(temp_node.left)
                if temp_node.right:
                    mylist.append(temp_node.right)
            res.append([level_list,level])
        return res[-1][0][0]