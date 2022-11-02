''''''
'''
问题描述
　　给定n个十六进制正整数，输出它们对应的八进制数。

输入格式
　　输入的第一行为一个正整数n （1<=n<=10）。
　　接下来n行，每行一个由0-9、大写字母A~F组成的字符串，表示要转换的十六进制正整数，每个十六进制数长度不超过100000。
　　
输出格式
　　输出n行，每行为输入对应的八进制正整数。
　　
【注意】
　　输入的十六进制数不会有前导0，比如012A。
　　输出的八进制数也不能有前导0。

样例输入
　　2
　　39
　　123ABC
样例输出
　　71
　　4435274　　
【提示】
　　先将十六进制数转换成某进制数，再由某进制数转换成八进制。
'''

while True:
    n = int(input())
    if n >= 1 and n <= 10:
        break

li = []
for i in range(n):
    while True:
        hex_num = input()
        if len(hex_num) <= 100000:
            break
    dec_num = int(hex_num, 16)  # int(hex_num, 16)把16进制的str转化成10进制
    oct_num = oct(dec_num)  # oct(dec_num)将10进制整数dec_num转化为八进制
    li.append(oct_num[2:])

for elem in li:
    print(elem)
