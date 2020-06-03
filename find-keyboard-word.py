def findWords(words):
    keyboard= ['qwertyuiop','asdfghjkl','zxcvbnm']
    res = []
    for i in words:
        temp = i.lower()
        for j in keyboard:
            if foo(temp,j):
                res.append(i)
    return res

def foo(word,keyboard):
    for i in word:
        if i not in keyboard:
            return False
    return True

s = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(s))
