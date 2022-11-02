''''''
'''
题目描述:
小明拥有N个彩灯，第i个彩灯的初始亮度为ai.
小明将进行Q次操作，每次操作可选择一段区间，并使区间内彩灯的亮度+x(x可能为负数)。求Q次操作后每个彩灯的亮度（若彩灯亮度为负数则输出O)。
输入描述
第一行包含两个正整数N，Q，分别表示彩灯的数量和操作的次数。
第二行包含N个整数，表示彩灯的初始亮度。
接下来Q行每行包含一个操作，格式如下:
l r x，表示将区间l～r的彩灯的亮度+x。
1 ≤ N, Q ≤ 5 × 10^5， 0 ≤ ai ≤ 10^9, 1 ≤ l ≤ r ≤ N，-10^9 < x ≤ 10^9
输出描述:
输出共1行，包含N个整数，表示每个彩灯的亮度。
'''
N, Q = map(int, input().split())
li = list(map(int, input().split()))
for i in range(1, N):
    li[i] -= li[i - 1]
for i in range(Q):
    l, r, x = map(int, input().split())
    li[l - 1] += x
    li[r] -= x
for i in range(1, N):
    li[i] += li[i - 1]
for elem in li:
    if elem < 0:
        print(0, end=' ')
    else:
        print(elem, end=' ')    