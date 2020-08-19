# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res_sum = []

        def help(root):
            if not root:
                return 0
            temp = root.val + help(root.left) + help(root.right)
            res_sum.append(temp)
            return temp

        if not root:
            return []
        help(root)
        res = []
        res_dict = {}
        for i in res_sum:
            if i not in res_dict:
                res_dict[i] = 1
            else:
                res_dict[i] += 1
        max_count = collections.Counter(res_sum).most_common(1)[0][1]
        for key, val in res_dict.items():
            if val == max_count:
                res.append(key)
        return res