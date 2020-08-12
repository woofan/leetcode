class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        res = 0
        while len(points) > 0:
            p = points.pop(0)
            start = p[0]
            end = p[1]
            while len(points) > 0:
                if points[0][0] <= end:
                    temp = points.pop(0)
                    start = max(start,temp[0])
                    end = min(end,temp[1])
                else:
                    break
            res += 1
        return res