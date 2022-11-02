''''''
'''
题目描述:
小蓝有一张黑白图像，由n x m个像素组成，其中从上到下共n行，每行从左到右m列。每个像素由一个0到255之间的灰度值表示。
现在，小蓝准备对图像进行模糊操作，操作的方法为:
对于每个像素，将以它为中心3×3区域内的所有像素（可能是9个像素或少于9个像素）求和后除以这个范围内的像素个数(取下整)，得到的值就是模糊后的结果。
请注意每个像素都要用原图中的灰度值计算求和。
输入描述:
输入的第一行包含两个整数n, m。
第⒉行到第n＋1行每行包含m个整数，表示每个像素的灰度值，相邻整数之间用一个空格分隔。其中，1 ≤n, m ≤100。
输出描述:
输出n行，每行m个整数，相邻整数之间用空格分隔，表示模糊后的图像。
'''
row, column = map(int, input().split())
gray_level_li = []
for _ in range(row):
    gray_level_li.append(list(map(int, input().split())))
new_li = [[0] * column for _ in range(row)]
for i in range(row):
    for j in range(column):
        tmp, cnt = 0, 0
        for m in range(i - 1, i + 2):
            for n in range(j - 1, j + 2):
                if m >= 0 and m < row and n >= 0 and n < column:
                    cnt += 1
                    tmp += gray_level_li[m][n]
        new_li[i][j] = tmp // cnt
for i in range(row):
    for j in range(column):
        print(new_li[i][j], end=' ')
    print()