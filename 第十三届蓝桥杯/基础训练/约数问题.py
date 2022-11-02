''''''
'''最大约数（不算本身）'''
def Max_Divisor(num):
    n = num // 2  # 1 * num = num, 从2开始递增找另一个可整除的数
    while True:
        if num % n == 0:
            print(n)
            if n == 1:
                print('It is a prime number!')
            break
        n -= 1
Max_Divisor(33)

'''最大公约数'''
def Max_Common_Divisor(num1, num2):  # num1 >= num2
    if num1 % num2 == 0:
        return num2
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2  # 辗转相除法
    return num2
mcd = Max_Common_Divisor(120, 72)
print(mcd)

'''最小公倍数'''
def Min_Common_Multiple(num1, num2):  # num1 >= num2:
    mcd = Max_Common_Divisor(num1, num2)
    mcm = num1 * num2 // mcd
    return mcm
mcm = Min_Common_Multiple(25, 120)
print(mcm)