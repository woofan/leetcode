class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mynums = sorted(nums)
        mydict = {}
        result = 0
        for i in mynums:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1
        keys = mydict.keys()
        keys = sorted(keys)
        for i in range(len(keys)-1):
            if keys[i+1] - keys[i] == 1:
                temp = mydict[keys[i]] + mydict[keys[i+1]]
                if temp > result:
                    result = temp
        return result