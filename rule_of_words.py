class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        key = 0
        for i in range(64):
            if n>>i & 1 == 1:
                key += 1
        if key == 1:
            return True
        else:
            return False
