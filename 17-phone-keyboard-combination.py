def letterCombinations(digits):
    keyboard = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    result = ['']
    digits_len = len(digits)
    if digits_len == 0:
        return []
    for i in range(digits_len):
        result = alphabatPremutationAndCombination(result,keyboard[digits[i]])
    return result

def alphabatPremutationAndCombination(list1,list2):
    res = []
    for i in list1:
        for j in list2:
            res.append(i+j)
    return res

print(letterCombinations('23'))