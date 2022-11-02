''''''
'''
A,2,3,4,5,6,7,8,9 共 9 张纸牌排成一个正三角形（A 按 1 计算）,要求每个边的和相等。
如果考虑旋转、镜像后相同的算同一种，一共有多少种不同的排法呢？
'''
from itertools import permutations
# 工具库(itertools)的全排列函数(permutations)
types = 0
for i in permutations(range(1, 10)):  # 列出所有情况
    a = i[0] + i[1] + i[2] + i[3]
    b = i[3] + i[4] + i[5] + i[6]
    c = i[6] + i[7] + i[8] + i[0]
    if a == b == c:  # 一个一个试
        types += 1
print(types // 6)  # 旋转➗3， 镜像➗2
