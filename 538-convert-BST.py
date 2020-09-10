# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def myhelp(root):
            if not root:
                return
            tree_element.append(root.val)
            if root.left:
                myhelp(root.left)
            if root.right:
                myhelp(root.right)

        def myfoo(root):
            if not root:
                return
            temp = 0
            for i in tree_element:
                if i > root.val:
                    temp += i
                else:
                    break
            temp += root.val
            root.val = temp
            if root.left:
                myfoo(root.left)
            if root.right:
                myfoo(root.right)

        if not root:
            return []
        tree_element = []
        myhelp(root)
        tree_element.sort(reverse=True)
        myfoo(root)
        return root