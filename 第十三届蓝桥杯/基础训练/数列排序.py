''''''
'''
资源限制
时间限制：1.0s 内存限制：512.0MB

问题描述
　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200

输入格式
　　第一行为一个整数n。
　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
输出格式
　　输出一行，按从小到大的顺序输出排序后的数列。

样例输入
5
8 3 6 4 9
样例输出
3 4 6 8 9
'''

while True:
    n = int(input())
    if n >= 1 and n <= 200:
        break

li = list(map(int, input().split()))

def Select_Sort(li):
    for i in range(len(li) - 1):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_idx]:
                min_idx = j
        li[min_idx], li[i] = li[i], li[min_idx]

Select_Sort(li)
for elem in li:
    print(elem, end=' ')
