def toHex(num):
    BtoH = {'0000':0,'0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'a','1011':'b','1100':'c','1101':'d','1110':'e','1111':'f'}
    res = ''
    if num == 0:
        res = '0'
    elif num > 0:
        binary = toBinary(num)
        add_zero = 4-(len(binary)%4)
        add_zero = 0 if add_zero==4 else add_zero
        for i in range(add_zero):
            binary = f'{0}{binary}'
        for i in range(len(binary)//4):
            temp = f'{binary[i*4]}{binary[i*4+1]}{binary[i*4+2]}{binary[i*4+3]}'
            res = f'{res}{BtoH[temp]}'
    elif num < 0:
        binary = toBinary(-num)
        binary_list = []
        for i in binary:
            binary_list.append(int(i))
        for i in range(len(binary_list)):
            binary_list[i] = 0 if binary_list[i] == 1 else 1
        binary_list[-1] += 1
        for i in range(len(binary_list)-1,-1,-1):
            if binary_list[i] == 2:
                binary_list[i] = 0
                if i-1>=0:
                    binary_list[i-1] += 1
        binary = ''
        for i in binary_list:
            binary = f'{binary}{i}'
        add_zero = 4 - (len(binary) % 4)
        add_zero = 0 if add_zero == 4 else add_zero
        for i in range(add_zero):
            binary = f'{0}{binary}'
        for i in range(len(binary)//4):
            temp = f'{binary[i*4]}{binary[i*4+1]}{binary[i*4+2]}{binary[i*4+3]}'
            res = f'{res}{BtoH[temp]}'
    return res


def toBinary(num):
    s = ''
    while num > 1:
        s = f'{num%2}{s}'
        num = num // 2
    s = f'{num}{s}'
    return s

print(toHex(-1))