''''''
'''
资源限制:
时间限制：1.0s 内存限制：256.0MB

问题描述:
Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少?
输入格式:
输入包含一个整数n。
输出格式:
输出一行，包含一个整数，表示Fn除以10007的余数。

说明：在本题中，答案是要求Fn除以10007的余数，因此我们只要能算出这个余数即可，而不需要先计算出Fn的准确值，再将计算的结果除以10007取余数，
     直接计算余数往往比先算出原数再取余简单。

样例输入:
10
样例输出:
55
样例输入:
22
样例输出:
7704
数据规模与约定:
1 <= n <= 1,000,000
'''

# 注意：先用递归或者其他方法计算出斐波那契数列值，再对10007取余会超时！

# 递归
def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

num1 = int(input('Please input num(num < 1000):'))  # Python的递归深度是有限的，默认是1000，当递归深度超过999时，就会引发异常
print(Fibonacci(num1))


while True:
    # 异常处理
    try:
        num2 = int(input())
        F1, F2 = 1, 1
        for i in range(3, num2 + 1):
            F1, F2 = F2 % 10007, (F1 + F2) % 10007  # 先取余再递推防止超时
            # print(F1, ' ', F2)
        print(F2)
    except:
        break
