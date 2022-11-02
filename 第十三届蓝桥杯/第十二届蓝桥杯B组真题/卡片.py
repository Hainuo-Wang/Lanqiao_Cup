''''''
'''
【问题描述】
小蓝有很多数字卡片，每张卡片上都是数字0到9。
小蓝准备用这些卡片来拼一些数，他想从1开始拼出正整数，每拼一个，就保存起来，卡片就不能用来拼其它数了。小蓝想知道自己能从1拼到多少。
例如，当小蓝有30张卡片，其中0到9各3张，则小蓝可以拼出1到10，但是拼11时卡片1已经只有一张了，不够拼出11。
现在小蓝手里有О到9的卡片各2021张，共20210张，请问小蓝可以从1拼到多少?
'''
'''
分析：卡片1会先被用完，或者不够用。
'''
from Calculate_Time import *

@Cal_Ti
def func1(num_cards):
    num = 0  # 记录要用掉卡片1的个数
    i = 0  # 要拼的数
    while True:
        i += 1
        num += str(i).count('1')
        if num == num_cards:  # 如果要拼的的这个数正好会把卡片1用完
            if str(i + 1).count('1') != 0:  # 如果下面的一个数还会用到卡片1，就只能拼到这个数
                print(i)
                break
            elif str(i + 1).count('1') == 0:  # 如果下面的数不会用到卡片1
                while True:
                    i += 1  # 接着往下拼
                    if str(i).count('1') == 1:  # 直到会用到1个卡片1
                        print(i - 1)
        elif num > num_cards:  # 剩余的卡片1不足以拼出这个数，只能拼到前一个数
            print(i - 1)
            break
func1(20210)

@Cal_Ti
def func2(num_cards):
    li = [0] * 10
    num = 0
    while True:
        num += 1
        for i in range(len(str(num))):
            li[int(str(num)[i])] += 1  # i是num的第i+1位数
        if max(li) > num_cards:
            print(num - 1)
            break
func2(20210)
