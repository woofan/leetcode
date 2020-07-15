def canConstruct(ransomNote, magazine):
    r = sorted(ransomNote)
    m = sorted(magazine)
    if len(r) > len(m):
        return False
    for i in range(len(r)-1,-1,-1):
        for j in range(len(m)):
            if r[i] == m[j]:
                r.pop(i)
                m.pop(j)
                break
        if i+1 == len(r):
            return False
    if len(r) != 0:
        return False
    else:
        return True

import collections
def canConstruct2(ransomNote, magazine):
    return False if (collections.Counter(ransomNote) - collections.Counter(magazine)) else True

print(canConstruct2('abccc','abcffcczz'))
