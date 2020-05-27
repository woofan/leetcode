class Solution:
    def isHappy(self, n: int) -> bool:
        mylist = []
        mylist.append(n)
        while self.foo(n) != 1:
            n = self.foo(n)
            if n in mylist:
                return False
            else:
                mylist.append(n)
        return True

    def foo(self, n):
        res = 0
        mylist = []
        while n > 0:
            mylist.append(n % 10)
            n = n // 10
        for i in mylist:
            res += i ** 2
        return res