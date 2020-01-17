class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        q =[]
        q.append(root)
        q.append(root)
        while len(q)>0:
            node1 = q.pop(0)
            node2 = q.pop(0)
            if node1 == None and node2 == None:
                continue
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        return True


root = TreeNode(2)
a = TreeNode(3)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
e = TreeNode(5)
f = TreeNode(4)
g = TreeNode(8)
h = TreeNode(9)
i = TreeNode(9)
j = TreeNode(8)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
d.left = g
d.right = h
f.left = i
f.right = j

s = Solution()
p = s.isSymmetric(root)
print(p)