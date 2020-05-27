class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        p = []
        l = len(s)
        for i in range(l+1):
            p.append(False)
        p[0] = True
        for i in range(l):
            for j in range(i+1,l+1):
                if p[i] and s[i:j] in wordDict:
                    p[j] = True
        return p[-1]