# 问题描述
# 　　求出区间[a,b]中所有整数的质因数分解。
# 输入格式
# 　　输入两个整数a，b。
# 输出格式
# 　　每行输出一个数的分解，形如k=a1a2a3…(a1<=a2<=a3…，k也是从小到大的)(具体可看样例)
# 样例输入
# 3 10
# 样例输出
# 3=3
# 4=22
# 5=5
# 6=23
# 7=7
# 8=222
# 9=33
# 10=25
# 提示
# 　　先筛出所有素数，然后再分解。
# 数据规模和约定
# 　　2<=a<=b<=10000
# 解题思路：
# 对一个数进行质因数分解
# 首先判断它本身是否为质数
# 是，则直接输出等于自身
# 否，进行循环，从2开始，输出最多的因数个数后才递增，这样保证不会有非质数因子
# 如，8 = 2 * 2 * 2
# 首先把最多的2输出，之后就不会出现2的倍数这样的因数啦。
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())
for i in range(a, b + 1):
    if is_prime(i):  # 如果是素数，则等于它本身
        print(i, '=', i, sep='')
    else:
        print(i, '=', sep='', end='')
        temp = i
        j = 2
        while temp > 1:
            if temp % j == 0:  # 分解质因数，从j=2开始除,直到对i取余不为0时，才j += 1，保证每个j出现最多
                temp = int(temp / j)
                print(j, end='')
                if temp != 1:
                    print('*', end='')
            else:
                j += 1
        print()
