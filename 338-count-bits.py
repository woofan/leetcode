class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(self.num_To_Binary(i))
        return res

    def num_To_Binary(self, num):
        tmp = 0
        while num > 1:
            tmp += num % 2
            num = num // 2
        return tmp + num