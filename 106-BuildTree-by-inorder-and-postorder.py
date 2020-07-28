# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def help(inorder_left, inorder_right, postorder_left, postorder_right):
            if postorder_left > postorder_right:
                return None
            postorder_root_index = postorder_right
            inorder_root_index = index[postorder[postorder_root_index]]
            left_subtree_num = inorder_root_index - inorder_left
            root = TreeNode(postorder[postorder_root_index])
            root.left = help(inorder_left, inorder_root_index - 1, postorder_left,
                             postorder_left + left_subtree_num - 1)
            root.right = help(inorder_root_index + 1, inorder_right, postorder_left + left_subtree_num,
                              postorder_right - 1)
            return root

        index = {}
        for i in range(len(inorder)):
            index[inorder[i]] = i
        return help(0, len(inorder) - 1, 0, len(postorder) - 1)
