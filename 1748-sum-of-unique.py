class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        my_dict = {}
        result = 0
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for key,val in my_dict.items():
            if val == 1:
                result += key
        return result