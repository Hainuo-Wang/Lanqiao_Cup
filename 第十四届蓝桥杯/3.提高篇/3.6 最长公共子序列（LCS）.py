# 问题描述
# 　　给定两个字符串，寻找这两个字串之间的最长公共子序列。
# 输入格式
# 　　输入两行，分别包含一个字符串，仅含有小写字母。
# 输出格式
# 　　最长公共子序列的长度。
# 样例输入
# abcdgh
# aedfhb
# 样例输出
# 3
# 样例说明
# 　　最长公共子序列为a，d，h。
# 数据规模和约定
# 　　字串长度1~1000。
# https://blog.csdn.net/weixin_40673608/article/details/84262695
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


a = input()

b = input()

print(lcs(a, b))


