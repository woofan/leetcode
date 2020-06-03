import math
def foo(n):
    if n == 0:
        return 0
    visited = set()
    q = [n]
    step = 0
    while len(q)>0:
        step += 1
        for i in range(len(q)):
            temp = q.pop()
            for j in range(1,int(math.sqrt(temp))+1):
                x = j**2
                if temp == x:
                    return step
                if (temp - x) not in visited:
                    q.insert(0,temp-x)
                    visited.add(temp-x)
    return step

print(foo(11))