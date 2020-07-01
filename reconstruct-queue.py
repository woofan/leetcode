a=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

def reconstructQueue(people):
    key_list = []
    mylist = []
    people = sorted(people,key=(lambda x:[x[0],x[1]]),reverse=False)
    for i in people:
        if i[0] not in key_list:
            key_list.append(i[0])
    key_list = sorted(key_list,reverse=True)
    for i in key_list:
        for j in people:
            if j[0] == i:
                mylist.append(j)
    key_list = []
    for i in range(len(mylist)):
        key_list.insert(mylist[i][1],mylist[i])
    return key_list
print(reconstructQueue(a))