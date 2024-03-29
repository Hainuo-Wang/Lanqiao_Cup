# 小明用字母A 对应数字1，B 对应2，以此类推，用Z 对应26。对于27
# 以上的数字，小明用两位或更长位的字符串来对应，例如AA 对应27，AB 对
# 应28，AZ 对应52，LQ 对应329。
# 请问2019 对应的字符串是什么？
"""
类似于进制转换，只是多了一步，把对应的字母换上
A~Z代表1~26，每26进1，27即为AA
17 77 Q
25 2 Y
2 0 B
BYQ
17 + 25 * 26 + 2 * 26 * 26 = 2019
"""

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = [0 for _ in range(5)]

index = 0

n = 2019

while n != 0:

    t = n % 26

    n = int(n / 26)

    ans[index] = string[t - 1]

    # print(t, n, ans[index])

    index += 1

for i in range(index - 1, -1, -1):

    print(ans[i], end='')

