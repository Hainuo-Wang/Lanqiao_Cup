# 问题描述
# 　　小明刚经过了一次数学考试，老师由于忙碌忘记排名了，于是老师把这个光荣的任务交给了小明，小明则找到了聪明的你，希望你能帮他解决这个问题。
# 输入格式
# 　　第一行包含一个正整数N，表示有个人参加了考试。接下来N行，每行有一个字符串和一个正整数，分别表示人名和对应的成绩，用一个空格分隔。
# 输出格式
# 　　输出一共有N行，每行一个字符串，第i行的字符串表示成绩从高到低排在第i位的人的名字，若分数一样则按人名的字典序顺序从小到大。
# 样例输入
# 3
# aaa 47
# bbb 90
# ccc 70
# 样例输出
# bbb
# ccc
# aaa 【数据规模和约定】
# 人数<=100,分数<=100,人名仅包含小写字母。
#
# 主要是对排序函数的利用
n = int(input())

information = [tuple(input().split()) for _ in range(n)]

information.sort(key=lambda x: x[0])  # 先排姓名，按字母顺序

information.sort(key=lambda x: int(x[1]),reverse=True)  # 后排成绩，从大到小

for i in range(n):
    print(information[i][0])


