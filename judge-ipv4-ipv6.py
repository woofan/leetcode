def validIPAddress(IP: str) -> str:
    temp1 = IP.split('.')
    temp2 = IP.split(':')
    flag1 = 0
    flag2 = 0
    if len(temp1) == 4:
        for i in temp1:
            if i == '':
                flag1 = -1
                break
            if len(i) > 3:
                flag1 = -1
                break
            if not i.isdigit():
                flag1 = -1
                break
            if len(i) > 1 and int(i[0]) == 0:
                flag1 = -1
                break
            if int(i) > 255:
                flag1 = -1
                break
    else:
        flag1 = -1
    if len(temp2) == 8:
        for i in temp2:
            if i == '':
                flag2 = -1
                break
            if len(i) > 4:
                flag2 = -1
                break
            if not i.isalnum():
                flag2 = -1
                break
            for j in i.lower():
                if j not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                    flag2 = -1
                    break

    else:
        flag2 = -1
    if flag1 == -1 and flag2 == -1:
        return 'Neither'
    if flag1 == 0 and flag2 == -1:
        return 'IPv4'
    if flag1 == -1 and flag2 == 0:
        return 'IPv6'


a = "192.0.0.1"
print(validIPAddress(a))