import collections
def getHint1(secret, guess):
    s = []
    g = []
    bull = 0
    cow = 0
    for i in secret:
        s.append(i)
    for i in guess:
        g.append(i)
    for i in range(len(s)):
        if s[i] == g[i]:
            bull += 1
            s[i] = None
            g[i] = ''
    for i in range(len(g)):
        for j in range(len(s)):
            if g[i] == s[j]:
                cow += 1
                s[j] = None
                break
    return '{}A{}B'.format(bull,cow)

def getHint(secret, guess):
    bull = 0
    cow = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
    s = dict(collections.Counter(secret))
    g = dict(collections.Counter(guess))
    for i in g.keys():
        if i in s:
            cow += min(s[i],g[i])
    cow -= bull
    return '{}A{}B'.format(bull, cow)
print(getHint('1122','0001'))