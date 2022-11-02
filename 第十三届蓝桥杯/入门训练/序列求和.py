from Calculate_Time import *
'''
问题描述:
求1+2+3+…+n的值。
输入格式:
输入包括一个整数n。
输出格式:
输出一行，包括一个整数，表示1+2+3+…+n的值。
'''

num = int(input())
@Cal_Ti
def List_Sum1(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum
@Cal_Ti
def List_Sum2(num):
    return 0.5 * num * num + 0.5 * num

print(List_Sum1(num))
print(List_Sum2(num))
