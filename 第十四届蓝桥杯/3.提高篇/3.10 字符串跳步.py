# 问题描述
# 　　给定一个字符串，你需要从第start位开始每隔step位输出字符串对应位置上的字符。
# 输入格式
# 　　第一行一个只包含小写字母的字符串。
#
# 第二行两个非负整数start和step，意义见上。
# 输出格式
# 　　一行，表示对应输出。
# 样例输入
# abcdefg
# 2 2
# 样例输出
# ceg
# 数据规模和约定
# 　　start从0开始计数。
# 　　字符串长度不超过100000。
s = input()

start, step = map(int, input().split())

print(s[start: : step])

