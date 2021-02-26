class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        A_dict = []
        for i in A:
            A_dict.append(self.cal_Char_Num(i))
        for i in A_dict[0].keys():
            tmp = A_dict[0][i]
            for j in A_dict[1:]:
                if i in j:
                    tmp = min(tmp,j[i])
                else:
                    tmp = 0
                    break
            for k in range(tmp):
                res.append(i)
        return res

    def cal_Char_Num(self,s):
        res = {}
        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        return res