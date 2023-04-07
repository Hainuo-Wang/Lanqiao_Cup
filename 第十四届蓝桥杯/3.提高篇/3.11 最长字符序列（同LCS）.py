# 问题描述
# 　　设x(i), y(i), z(i)表示单个字符，则X={x(1)x(2)……x(m)}，Y={y(1)y(2)……y(n)}，Z={z(1)z(2)……z(k)},我们称其为字符序列，其中m,n和k分别是字符序列X，Y，Z的长度，括号()中的数字被称作字符序列的下标。
# 　　如果存在一个严格递增而且长度大于0的下标序列{i1,i2……ik}，使得对所有的j=1,2,……k，有x(ij)=z(j)，那么我们称Z是X的字符子序列。而且，如果Z既是X的字符子序列又是Y的字符子序列，那么我们称Z为X和Y的公共字符序列。
# 　　在我们今天的问题中，我们希望计算两个给定字符序列X和Y的最大长度的公共字符序列，这里我们只要求输出这个最大长度公共子序列对应的长度值。
# 　　举例来说，字符序列X=abcd，Y=acde，那么它们的最大长度为3，相应的公共字符序列为acd。
# 输入格式
# 　　输入一行，用空格隔开的两个字符串
# 输出格式
# 　　输出这两个字符序列对应的最大长度公共字符序列的长度值
# 样例输入
# aAbB aabb
# 样例输出
# 2
# 数据规模和约定
# 　　输入字符串长度最长为100，区分大小写。
def lcs(str_a, str_b):
    len_a = len(a)
    len_b = len(b)
    arr = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]
    for i in range(len_a + 1):
        for j in range(len_b + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif i > 0 and j > 0 and str_a[i - 1] == str_b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
    return arr[len_a][len_b]


a, b = input().split()

print(lcs(a, b))


