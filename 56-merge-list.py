def merge(intervals):
    intervals = sorted(intervals)
    for i in range(len(intervals)-1):
        if intervals[i+1][0] <= intervals[i][1]:
            if intervals[i+1][1] <= intervals[i][1]:
                intervals[i+1] = intervals[i]
                intervals[i] = []
            elif intervals[i+1][1] > intervals[i][1]:
                intervals[i+1] = [intervals[i][0],intervals[i+1][1]]
                intervals[i] = []
    res = []
    for i in intervals:
        if i != []:
            res.append(i)
    return res

a=[[1,3],[2,6],[8,10],[15,18]]
print(merge(a))
