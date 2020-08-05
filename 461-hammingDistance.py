class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = self.intToBinary(x)
        y = self.intToBinary(y)
        res = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1
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
        if n < 0:
            for i in range(32):
                binary_n[i] = 0 if binary_n[i] == 1 else 1
            binary_n[-1] += 1
            for i in range(31, -1, -1):
                if binary_n[i] > 1:
                    binary_n[i] = 0
                    if i - 1 >= 0:
                        binary_n[i - 1] += 1
        return binary_n

