class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        total_0 = [0] * 32
        total_1 = [0] * 32
        for i in nums:
            temp = self.intToBinary(i)
            for j in range(32):
                if temp[j] == 0:
                    total_0[j] += 1
                else:
                    total_1[j] += 1
        for i in range(32):
            res += total_0[i] * total_1[i]
        return res

    def intToBinary(self, n):
        abs_n = abs(n)
        binary_n = []
        while abs_n != 0:
            temp = abs_n % 2
            abs_n //= 2
            binary_n.insert(0, temp)
        for i in range(32 - len(binary_n)):
            binary_n.insert(0, 0)
        return binary_n