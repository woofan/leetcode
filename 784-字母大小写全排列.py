# coding:utf-8
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s_list = [i for i in s]
        word_index = []
        word = ''
        ans = []
        for i in range(len(s_list)):
            if not s_list[i].isdigit():
                word_index.append(i)
                word += s_list[i]
        if word == '':
            return [s]
        all_words = self.getAllWords(word.lower())
        for oneword in all_words:
            for i, index in enumerate(word_index):
                s_list[index] = oneword[i]
            ans.append(''.join(s_list))
        return ans

    #全排列所有s字符串的大小写组合,位置不变，传入的s均为小写
    def getAllWords(self, s):
        if len(s) == 1:
            return [s, s.upper()]
        ans = []
        for i in self.getAllWords(s[1:]):
            ans.append(s[0] + i)
            ans.append(s[0].upper() + i)

