def originalDigits(s):
    digits_dic = {'zero':0,'one':0,'two':0,'three':0,'four':0,'five':0,'six':0,'seven':0,'eight':0,'nine':0}
    character_dict = {'e':0,'f':0,'g':0,'h':0,'i':0,'n':0,'o':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'z':0}
    for i in s:
        character_dict[i] += 1
    digits_dic['zero'] = character_dict['z']
    digits_dic['two'] = character_dict['w']
    digits_dic['four'] = character_dict['u']
    digits_dic['six'] = character_dict['x']
    digits_dic['eight'] = character_dict['g']
    digits_dic['three'] = character_dict['h'] - digits_dic['eight']
    digits_dic['five'] = character_dict['f'] - digits_dic['four']
    digits_dic['one'] = character_dict['o'] - digits_dic['zero'] - digits_dic['two'] - digits_dic['four']
    digits_dic['seven'] = character_dict['v'] - digits_dic['five']
    digits_dic['nine'] = character_dict['i'] - digits_dic['six'] - digits_dic['eight'] - digits_dic['five']
    res = ''
    for i in [['zero',0],['one',1],['two',2],['three',3],['four',4],['five',5],['six',6],['seven',7],['eight',8],['nine',9]]:
        for j in range(digits_dic[i[0]]):
            res = f'{res}{i[1]}'
    return res

print(originalDigits('owoztneoer'))