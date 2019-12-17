def isalindrome(x):
    x_str = str(x)
    x_len = len(x_str)
    flag = True
    for i in range(x_len//2+1):
        if x_str[i] != x_str[-(i+1)]:
            flag = False
            break
    return flag

print(isalindrome(12321))