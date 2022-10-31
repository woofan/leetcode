#coding:utf-8
class Solution:
    def magicalString(self, n: int) -> int:
        magical = '122'
        add_num = ['1','2']
        index = 2
        while len(magical) < n:
             magical += str(add_num[index%2] * int(magical[index]))
             index += 1
        count = 0
        for i in magical[:n]:
            if i  == '1':
                count += 1
        return count