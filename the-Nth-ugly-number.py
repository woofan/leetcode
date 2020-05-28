def theNthUgly(num):
    if num <1 or num >1690:
        return None
    ugly_dict = {}
    ugly_index = 0
    ugly_list = [1]
    factor = [2,3,5]
    while ugly_index <= 1690:
        min_ugly = ugly_list.pop(0)
        ugly_index += 1
        ugly_dict[ugly_index] = min_ugly
        for i in factor:
            temp = min_ugly * i
            if temp not in ugly_list:
                ugly_list.append(temp)
        ugly_list.sort()
    print(ugly_dict)
    return ugly_dict[num]

print(theNthUgly(6))