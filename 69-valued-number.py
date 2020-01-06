def isNumber(s):
    flag = isValue(s)
    if not flag:
        return False
    if 'e' in s:
        return isScientificCount(s)
    elif '.' in s:
        return isDecimal(s)
    else:
        return isInteger(s)

def isScientificCount(s):
    x,y = s.split('e',1)
    try:
        x = float(x)
    except:
        return False
    if '.' in y:
        return False
    else:
        try:
            y = int(y)
        except:
            return False
    return True

def isDecimal(s):
    try:
        x = float(s)
    except:
        return False
    return True

def isInteger(s):
    try:
        x = int(s)
    except:
        return False
    return True

def isValue(s):
    x = s.split(' ')
    if len(x)>1:
        return False
    else:
        return True
