# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def myhelp(root):
            if not root:
                return 0

            left_tilt = myhelp(root.left)
            right_tilt = myhelp(root.right)
            tilt = abs(left_tilt - right_tilt)
            self.res += tilt
            return root.val + left_tilt + right_tilt

        myhelp(root)
        return self.res
