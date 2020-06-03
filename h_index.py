class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = [0]
        for i in citations:
            temp = 0
            for j in citations:
                if j >= i:
                    temp += 1
            res.append(temp if temp<=i else i)
        return max(res)