def hIndex(citations):
    res = 0
    for i in range(len(citations)):
        k = citations[i] if citations[i] <= (len(citations) - i) else len(citations) - i
        res = res if res >= k else k
    return res

a = [0,1,3,5,6]
print(hIndex(a))