# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        temp_res = []
        mylist = [root]
        level = 0
        while len(mylist) > 0:
            level += 1
            level_list = []
            for i in range(len(mylist)):
                temp_node = mylist.pop(0)
                level_list.append(temp_node.val)
                if temp_node.left:
                    mylist.append(temp_node.left)
                if temp_node.right:
                    mylist.append(temp_node.right)
            temp_res.append([level,level_list])
        for i in temp_res:
            res.append(max(i[1]))
        return res