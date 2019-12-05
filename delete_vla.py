def func(x):
    x_str = str(x)
    x_len = len(x_str)
    flag = True
    for i in range(x_len//2):
        if x_str[i] != x_str[-i]:
            flag = False
            break
    return flag