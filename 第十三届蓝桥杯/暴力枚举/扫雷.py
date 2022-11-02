''''''
'''
题目描述:
在一个n行m列的方格图上有一些位置有地雷，另外一些位置为空。
请为每个空位置标一个整数，表示周围八个相邻的方格中有多少个地雷。
输入描述:
输入的第一行包含两个整数n, m。
第2行到第n＋1行每行包含m个整数，相邻整数之间用一个空格分隔。如果对应的整数为0，表示这一格没有地雷。
如果对应的整数为1，表示这一格有地雷。其中，1 ≤ n, m ≤ 100。
输出描述:
输出n行，每行m个整数，相邻整数之间用空格分隔。
对于没有地雷的方格，输出这格周围的地雷数量。对于有地雷的方格，输出9。
'''
row, column = map(int, input().split())
li = []
for _ in range(row):
    li.append(list(map(int, input().split())))
new_li = [[0] * column for _ in range(row)]
for i in range(row):
    for j in range(column):
        if li[i][j] == 1:
            new_li[i][j] = 9
        else:
            for m in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                     if m >= 0 and m < row and n >= 0 and n < column:
                         new_li[i][j] += li[m][n]
for i in range(row):
    for j in range(column):
        print(new_li[i][j], end=' ')
    print()
