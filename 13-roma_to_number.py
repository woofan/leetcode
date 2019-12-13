def number_to_roman(n):
    roman_dict = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',5:'V',50:'L',500:'D','thousand_place':'M','hundred_place':'C','ten_place':'X','one_place':'I'}
    temp_dict = {'hundred_place':100,'ten_place':10,'one_place':1}
    number_dict = {}
    result = ''
    thousand_place= n//1000
    hundred_place = (n%1000)//100
    ten_place = ((n%1000)%100)//10
    one_place = n%10
    number_dict['thousand_place'] = thousand_place
    number_dict['hundred_place'] = hundred_place
    number_dict['ten_place'] = ten_place
    number_dict['one_place'] = one_place
    for k,v in number_dict.items():
        if v==4 or v==9 or v==5:
            result += roman_dict[temp_dict[k]*v]
        elif v>=1 and v<=3:
            for i in range(v):
                result += roman_dict[k]
        elif v>5 and v<9:
            v1 = v-5
            v2 = 5
            result += roman_dict[temp_dict[k]*v2]
            for i in range(v1):
                result += roman_dict[k]
    return result

print(number_to_roman(1994))
