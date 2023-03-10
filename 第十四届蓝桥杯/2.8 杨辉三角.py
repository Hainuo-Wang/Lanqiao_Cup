# 问题描述
#
# 杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
#
# 它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
#
# 下面给出了杨辉三角形的前4行：
#
# 1
#
# 1 1
#
# 1 2 1
#
# 1 3 3 1
#
# 给出n，输出它的前n行。
# 输入格式
#
# 输入包含一个数n。
# 输出格式
# 输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
# 样例输入
# 4
# 样例输出
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 数据规模与约定
# 1 <= n <= 34。

n = int(input())
k = 2
triangle_yang = []  # 杨辉三角
for i in range(n):  # 定义空的杨辉三角
    triangle_yang.append([0 for j in range(i + 1)])
for i in range(n):
    triangle_yang[i][0] = triangle_yang[i][-1] = 1
while k < n:
    m = 1
    while m < k:  # 两肩数值之和
        triangle_yang[k][m] = triangle_yang[k - 1][m - 1] + triangle_yang[k - 1][m]
        m += 1
    k += 1
for i in range(n):
    for j in range(i + 1):
        print(triangle_yang[i][j], end=' ')
    print()
