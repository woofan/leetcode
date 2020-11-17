import collections
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        p = collections.Counter(candies).most_common()
        most_len = len(p)
        if most_len <= len(candies)//2:
            return most_len
        else:
            return len(candies)//2