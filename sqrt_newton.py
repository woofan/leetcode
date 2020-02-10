'''
用牛顿法求解正数的开方
设正数为 n
问题可以等效与求解f(x)=x^2-n的零点
泰勒一阶展开：f(x)=f(x0)+f(x0)的导数 * (x - x0)
令f(x)=0,有x=x0 - f(x0)/f(x0)的导数
对于f(x)，导数为2x，求得：x=(x0 + n/x0)/2
'''
def sqrtByNewtonMethod(number,accuracy):
    if number<0:
        return false
    if number == 0:
        return 0
    x = number/2
    while abs(number - x*x) > accuracy:
        x = (x+number/x)/2
    return x

