''''''
'''
问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。　　
下面给出了杨辉三角形的前4行：
　　
1　　
1 1　　
1 2 1
1 3 3 1　　
给出n，输出它的前n行。
输入格式
输入包含一个数n。
输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
样例输入
4
样例输出
1
1 1
1 2 1
1 3 3 1
'''

n = int(input())

li = [[0] * n for i in range(n)]  # 初始化一个n * n的矩阵

for i in range(n):
    for j in range(n):
        if j == 0:
            li[i][j] = 1
        else:
            li[i][j] = li[i - 1][j - 1] + li[i - 1][j]
        if li[i][j] != 0:
            if i == j:
                print(li[i][j])
            else:
                print(li[i][j], end=' ')

'''
tri_li = []
row = 0
while True:
    row_li = []
    row += 1  # 第几行
    for i in range(row):
        if i == 0 or i == (row - 1):
            row_li.append(1)
        else:
            if row > 2 and i >= 1:
                row_li.append(tri_li[row - 2][i - 1] + tri_li[row - 2][i])
    tri_li.append(row_li)
    if row == n:
        break

for elem in range(tri_li):
    print(elem)
'''