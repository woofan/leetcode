class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 999999
        temp = [] #transfer to miniutes
        for i in timePoints:
            hour,miniutes = i.split(":")
            temp.append(int(hour)*60 + int(miniutes))
        temp.sort()
        for i in range(len(temp)-1):
            if temp[i+1] - temp[i] < res:
                res = temp[i+1] - temp[i]
        p = 24*60 - temp[-1] + temp[0]
        if res > p:
            res = p
        return res