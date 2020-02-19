class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def preOrder(self,Node):#非递归先序遍历
        current = Node
        res = []
        q = []
        while current or q:
            if current:
                res.append(current.val)
                q.append(current.right)
                current = current.left
            else:
                current = q.pop()
        return res


    def postOrder(self,Node):#非递归后序遍历
        current = Node
        res = []
        q = []
        while q or current:
            if current:
                res.append(current.val)
                q.append(current.left)
                current = current.right
            else:
                current = q.pop()
        return res[::-1]

    def inOrder(self,Node):#非递归中序遍历
        current = Node
        res = []
        q = []
        while q or current:
            if current:
                q.append(current)
                current = current.left
            else:
                current = q.pop()
                res.append(current.val)
                current = current.right
        return res

    def levelOrder(self,Node):#非递归层序遍历
        q = []
        res = []
        level = 0
        q.append(Node)
        while len(q) > 0:
            level_list = []
            level += 1
            for i in range(len(q)):
                tmp = q.pop(0)
                level_list.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            res.append([level,level_list])
        return res

    def invertBinaryTree(self,Node):
        q = []
        current = Node
        q.append(current)
        while q:
            n = q.pop(0)
            tmp = n.left
            n.left = n.right
            n.right = tmp
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return Node

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5


s = Solution()
t1 = s.invertBinaryTree(t1)
print(s.preOrder(t1))
print(s.inOrder(t1))
print(s.postOrder(t1))
#print(s.levelOrder(t1))