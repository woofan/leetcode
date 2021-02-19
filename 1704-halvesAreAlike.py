class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_list = ['a','e','i','o','u']
        s = s.lower()
        vowel_char_1 = 0
        vowel_char_2 = 0
        for i in range(len(s)//2):
            if s[i] in vowel_list:
                vowel_char_1 += 1
            if s[-(i+1)] in vowel_list:
                vowel_char_2 += 1
        if vowel_char_1 == vowel_char_2:
            return True
        else:
            return False