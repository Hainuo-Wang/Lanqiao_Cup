# 问题描述
# 　　回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。
# 输入格式
# 　　输入第一行是两个不超过200的正整数m, n，表示矩阵的行和列。接下来m行每行n个整数，表示这个矩阵。
# 输出格式
# 　　输出只有一行，共mn个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。
# 样例输入
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 样例输出
# 1 4 7 8 9 6 3 2 5
# 样例输入
# 3 2
# 1 2
# 3 4
# 5 6
# 样例输出
# 1 3 5 6 4 2
m, n = map(int, input().split())
row = col = count = 0
matrix = [[] for _ in range(m)]
for i in range(m):
    arr = input().split()
    for j in range(n):
        matrix[i].append(int(arr[j]))
while count < m * n:  # 总共m*n个数
    while row < m and matrix[row][col] != -1:  # 向下取数
        print(matrix[row][col], end=' ')
        matrix[row][col] = -1  # 将去过的位置置为-1
        row += 1
        count += 1
    row -= 1  # 上个循环结束后row的值为m,需要减1，否则越界
    col += 1  # 列值加1，因为第零列在上个循环已经输出，往右推一行
    while col < n and matrix[row][col] != -1:  # 向右取数
        print(matrix[row][col], end=' ')
        matrix[row][col] = -1  # 将去过的位置置为-1
        col += 1
        count += 1
    row -= 1  # 往上推一行
    col -= 1  # 上个循环使列值为n
    while row >= 0 and matrix[row][col] != -1:  # 向上取数
        print(matrix[row][col], end=' ')
        matrix[row][col] = -1  # 将去过的位置置为-1
        row -= 1
        count += 1
    row += 1  # 上个循环使行值为-1
    col -= 1  # 往左推一行
    while col >= 0 and matrix[row][col] != -1:  # 向左取数
        print(matrix[row][col], end=' ')
        matrix[row][col] = -1  # 将去过的位置置为-1
        col -= 1
        count += 1
    col += 1  # 上个循环使列值为-1
    row += 1  # 向下推一行
