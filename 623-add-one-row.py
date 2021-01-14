# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            tmp = root
            root  = TreeNode(v)
            root.left = tmp
        else:
            q = []
            level = 0
            q.append(root)
            while q:
                level_list = []
                level += 1
                if level != (d -1):
                    for i in range(len(q)):
                        tmp = q.pop(0)
                        if tmp.left:
                            q.append(tmp.left)
                        if tmp.right:
                            q.append(tmp.right)
                else:
                    for i in range(len(q)):
                        tmp = q.pop(0)
                        if tmp.left:
                            n = TreeNode(v)
                            n.left = tmp.left
                            tmp.left = n
                        else:
                            n = TreeNode(v)
                            tmp.left = n
                        if tmp.right:
                            n = TreeNode(v)
                            n.right = tmp.right
                            tmp.right = n
                        else:
                            n = TreeNode(v)
                            tmp.right = n
                    break
        return root