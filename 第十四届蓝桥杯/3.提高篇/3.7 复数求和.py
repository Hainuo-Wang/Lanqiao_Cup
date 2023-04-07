# 从键盘读入n个复数（实部和虚部都为整数）用链表存储，遍历链表求出n个复数的和并输出。
# 样例输入:
# 3
# 3 4
# 5 2
# 1 3
# 样例输出:
# 9+9i
#
# 样例输入:
# 7
# 1 2
# 3 4
# 2 5
# 1 8
# 6 4
# 7 9
# 3 7
# 样例输出:
# 23+39i
n = int(input())

real = 0

imaginary = 0

com = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    real += com[i][0]
    imaginary += com[i][1]

print(real, '+', imaginary, 'i', sep='')

