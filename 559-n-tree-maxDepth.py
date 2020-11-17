"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        result = 0
        mylist = [root]
        while len(mylist) != 0:
            result += 1
            for i in range(len(mylist)):
                temp = mylist.pop()
                if len(temp.children) > 0:
                    for child in temp.children:
                        mylist.insert(0,child)
        return result