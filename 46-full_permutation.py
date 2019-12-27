def permute(num_list):
    tmp = []
    for i in num_list:
        tmp = help(i,tmp)
    return tmp

def help(new_num,old_list):
    old_list_len = len(old_list)
    if old_list_len == 0:
        return [[new_num]]
    else:
        res = []
        for i in old_list:
            last_one = i.copy()
            last_one.append(new_num)
            for j in range(len(i)):
                tmp = i.copy()
                tmp.insert(j,new_num)
                res.append(tmp)
            res.append(last_one)
        return  res

print (permute([1,2,3,4]))