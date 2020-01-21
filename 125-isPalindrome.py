def isPalindrome(s):
    tmp = []
    s = s.lower()
    for i in s:
        if 48<= ord(i) <=57 or 97<=ord(i)<=122:
            tmp.append(i)
    half = len(tmp)//2
    for i in range(half):
        if tmp[i] != tmp[-i-1]:
            return False
    return True


print (isPalindrome('abc defedcba'))