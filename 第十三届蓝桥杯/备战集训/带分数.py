''''''
'''
题目描述:
100 可以表示为带分数的形式:100 = 3 + 69258 / 714, 还可以表示为:100 = 82 + 3546 / 197
注意特征:带分数中，数字1~9分别出现且只出现一次(不包含0)。类似这样的带分数，100有11种表示法。
输入描述:
从标准输入读入一个正整数N (N < 1000 x 1000)。
输出描述:
程序输出该数字用数码1~9不重复不遗漏地组成带分数表示的全部种数。
注意:不要求输出每个表示，只统计有多少表示法!
'''
from itertools import permutations
n = int(input())
num = 0
# for case in permutations('123456789+/'):
#     s = ''.join(case)
#     if s.index('+') > 0 and s.index('/') < 10 and s.index('/') - s.index('+') > 1 and eval(s) == n:
#         num += 1
# print(num)
# 超时严重

'''
n = a + b // c
b = (n - a) * c
b[-1] = (n - a) * c[-1] % 10
'''
for case in permutations('123456789'):
    s = ''.join(case)  # case:list -> s:str
    c_last = int(s[-1])
    for i in range(len(str(n))):  # (n - a) > 0
        a = int(s[: i + 1])
        b_last = (n - a) * int(s[-1]) % 10
        if b_last == 0:
            continue
        b_last_index = s.index(str(b_last))
        if b_last_index <= i or b_last_index >= 8:
            continue
        b = int(s[i + 1: b_last_index + 1])
        c = int(s[b_last_index + 1:])
        if a + b / c == n:
            num += 1
print(num)
