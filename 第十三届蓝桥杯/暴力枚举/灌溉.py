''''''
'''
题目描述:
小蓝负责花园的灌溉工作。
花园可以看成一个n行m列的方格图形。中间有一部分位置上安装有出水管。
小蓝可以控制一个按钮同时打开所有的出水管，打开时，有出水管的位置可以被认为已经灌溉好。
每经过一分钟，水就会向四面扩展一个方格，被扩展到的方格可以被认为已经灌溉好。即如果前一分钟某一个方格被灌溉好，则下一分钟它上下左右的四个方格也被灌溉好。
给定花园水管的位置，请问k分钟后，有多少个方格被灌溉好?
输入描述:
输入的第一行包含两个整数n, m。
第二行包含一个整数t，表示出水管的数量。
接下来t行描述出水管的位置，其中第i行包含两个数r, c表示第r行第c列有一个排水管。接下来一行包含一个整数k。
其中，1 ≤ n, m ≤ 100, 1 < t ≤ 10, 1 ≤ k ≤ 100。
输出描述:
输出一个整数，表示答案。
'''
row, column = map(int, input().split())
grid = [[0] * column for i in range(row)]
tmp = [[0] * column for j in range(row)]  # 不能直接tmp = grid
pipe_num = int(input())
for cnt in range(pipe_num):
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = 1
minute = int(input())

for counter in range(minute):
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                tmp[i][j] = 1
                if i > 0:
                    tmp[i - 1][j] = 1
                if i < row - 1:
                    tmp[i + 1][j] = 1
                if j > 0:
                    tmp[i][j - 1] = 1
                if j < column - 1:
                    tmp[i][j + 1] = 1
    grid = tmp

num = 0
for i in grid:
    for j in i:
        num += j
print(num)