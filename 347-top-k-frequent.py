import collections
def topKFrequent(nums, k):
    res = []
    a = collections.Counter(nums).most_common(k)
    for i in a:
        res.append(i[0])
    return res

#print(topKFrequent([1,1,1,2,2,3],2))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        counter = sorted(counter.items(),key = lambda x:x[1], reverse = True)
        for i in range(k):
            res.append(counter[i][0])
        return res

a = {2:2,3:1,1:3}
a = sorted(a.items(),key=lambda x:x[1], reverse=True)
print(a)