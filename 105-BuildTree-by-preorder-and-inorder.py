# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def help(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            preorder_root_index = preorder_left
            inorder_root_index = index[preorder[preorder_root_index]]
            root = TreeNode(preorder[preorder_root_index])
            left_subtree_num = inorder_root_index - inorder_left
            root.left = help(preorder_left + 1, preorder_left + left_subtree_num, inorder_left, inorder_root_index - 1)
            root.right = help(preorder_left + left_subtree_num + 1, preorder_right, inorder_root_index + 1,
                              inorder_right)
            return root

        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        return help(0, len(preorder) - 1, 0, len(inorder) - 1)