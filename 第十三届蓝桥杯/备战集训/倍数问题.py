''''''
'''
众所周知，小葱同学擅长计算，尤其擅长计算一个数是否是另外一个数的倍数。但小葱只擅长两个数的情况，当有很多个数之后就会比较苦恼。
现在小葱给了你 n 个数，希望你从这 n 个数中找到三个数，使得这三个数的和是 K 的倍数，且这个和最大。数据保证一定有解。

输入描述:
第一行包括2个正整数n，K。
第二行n个正整数，代表给定的n个数。
其中，1 ≤ n ≤ 10^5,1 ≤ K ≤ 10^3，给定的n个数均不超过10^8。
输出描述:
输出一行一个整数代表所求的和。
'''
from itertools import combinations  # 组合数函数
n, k = map(int, input().split())
li = sorted(list(map(int, input().split())), reverse=True)
max_sum = 0
for cmb in combinations(li, 3):
    tmp = sum(cmb)
    if tmp % k == 0 and tmp > max_sum:
        max_sum = tmp
print(max_sum)
# 暴力破解，运行超时。
# 得分：30

'''
from itertools import combinations  # 组合数函数
n, k = map(int, input().split())
li = sorted(list(map(int, input().split())), reverse=True)

for cmb in combinations(li, 3):
    tmp = sum(cmb)
    if tmp % k == 0:
        print(tmp)
        break
# 答案错误
# 得分：50
'''


