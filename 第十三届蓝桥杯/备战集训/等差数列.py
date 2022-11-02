''''''
'''
题目
数学老师给小明出了一道等差数列求和的题目。但是粗心的小明忘记了一部分的数列，只记得其中 N 个整数。
现在给出这 N 个整数，小明想知道包含这 N 个整数的最短的等差数列有几项？

输入描述:
输入的第一行包含一个整数N。
第二行包含N个整数A1,A2,.. ,AN。(注意A ~ AN并不一定是按等差数列中的顺序给出)
其中，2 ≤ N ≤ 10^5，0 ≤ Ai ≤ 10^9。
输出描述:
输出一个整数表示答案。

输入:
5
2 6 4 10 20
输出:
10
'''
n = int(input())
li = sorted(list(map(int, input().split())))
tolerance = li[-1] - li[0]  # 开始设置为最大值和最小值的差

for idx in range(len(li) - 1):
    if li[idx + 1] - li[idx] < tolerance:  # 寻找已给数列中的最小差
        tolerance = li[idx + 1] - li[idx]

if tolerance == 0:
    print(len(li))
else:
    print(len(list(range(li[0], li[-1], tolerance))) + 1)
