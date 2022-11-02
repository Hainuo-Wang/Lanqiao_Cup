''''''
'''
题目描述
输入一个正整数n，输出n!的值。
其中n!=123*…*n。
算法描述
n!可能很大，而计算机能表示的整数范围有限，需要使用高精度计算的方法。使用一个数组A来表示一个大整数a，A[0]表示a的个位，A[1]表示a的十位，依次类推。
将a乘以一个整数k变为将数组A的每一个元素都乘以k，请注意处理相应的进位。
首先将a设为1，然后乘2，乘3，当乘到n时，即得到了n!的值。
输入:
输入包含一个正整数n，n< =1000。
输出:
输出n!的准确值。
'''

# 采用数组存储形式
n = int(input())
li = [1]  # 赋初值，不然无法启动
def Loop(n):
    global li
    for i in range(len(li)):  # 正常乘法， 每位各自乘
        li[i] *= n
    for i in range(len(li) - 1):  # 进位，但是首位进位不在此列
        li[i + 1] += int(li[i] / 10)
        li[i] %= 10
    li_1 = list(str(li[-1]))  # 分解首项
    li.pop()  # 删除首项
    for i in range(len(li_1) - 1, -1, -1):  # 倒序归入原序列
        li.append(int(li_1[i]))
for i in range(2, n + 1):  # n!定义
    Loop(i)
for i in range(len(li)):  # 转化形式
    li[i] = str(li[i])
print(''.join(li[::-1]))
