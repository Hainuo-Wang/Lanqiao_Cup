''''''
'''
杨辉三角形：
如果我们按从上到下、从左到右的顺序把所有数排成一列，可以得到如下数列：
1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, ...
给定一个正整数 N，请你输出数列中第一次出现 N 是在第几个数？
'''



'''
得分：45
N = int(input())  # 给定正整数
last_line = []
row = 0
temp = 0
flag = 0
while True:
    row_li = []
    row += 1  # 第几行
    for i in range(row):
        if i == 0 or i == (row - 1):
            temp = 1
            row_li.append(temp)
        else:
            if row > 2 and i >= 1:
                temp = last_line[i - 1] + last_line[i]
                row_li.append(temp)
        if temp == N:
            print(int(0.5 * (row - 1) * (row - 1) + 0.5 * (row - 1) + i + 1))
            flag = 1
            break
    if flag == 1:
        break
    last_line = row_li
'''

'''
得分：18
N = int(input())  # 给定正整数
last_line = []
row = 0
temp = 0
flag = 0
while True:
    row_li = []
    row += 1  # 第几行
    if row % 2 == 1:
        n = row // 2 + 1
    elif row % 2 == 0:
        n = row // 2
    for i in range(n):
        if i == 0:
            temp = 1
            row_li.append(temp)
        elif i >= 1:
            if row % 2 == 1:
                temp = last_line[i - 1] * 2
                row_li.append(temp)
            elif row % 2 == 0:
                temp = last_line[i - 1] + last_line[i]
                row_li.append(temp)
        if temp == N:
            print(int(0.5 * (row - 1) * (row - 1) + 0.5 * (row - 1) + i + 1))
            flag = 1
            break
    if flag == 1:
        break
    last_line = row_li
'''