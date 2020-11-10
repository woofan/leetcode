class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split(' ')
        result = ''
        for i in words_list:
            i = i[::-1]+' '
            result += i
        return result.strip()