def func(l,x):
    l.append(x)
    l = sorted(l)
    return l.index(x)

print(func([1,3,5,6],2))