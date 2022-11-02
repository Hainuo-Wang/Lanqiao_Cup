''''''
import datetime

'''
题目描述:
2020年春节期间，有一个特殊的日期引起了大家的注意:2020年2月2日。因为如果将这个日期按“yyyymmdd”的格式写成一个8位数是20200202，恰好是一个回文数。
我们称这样的日期是回文日期。
有人表示20200202是“千年一遇”的特殊日子。对此小明很不认同，因为不到2年之后就是下一个回文日期:20211202即2021年12月2日。
也有人表示20200202并不仅仅是一个回文日期，还是一个ABABBABA型的回文日期。
对此小明也不认同，因为大约100年后就能遇到下一个ABABBABA型的回文日期:21211212即2121年12月12日。算不上“千年一遇”，顶多算“千年两遇”。
给定一个8位数的日期，请你计算该日期之后下一个回文日期和下一个ABABBABA型的回文日期各是哪一天。
输入描述:
输入包含一个八位整数N，表示日期。
输出描述:
输出两行，每行1个八位数。第一行表示下一个回文日期，第二行表示下一个ABABBABA型的回文日期。
'''
n = input()
start_year = int(n[: 4])
start_month = int(n[4: 6])
start_day = int(n[6:])
start_date = datetime.date(start_year, start_month, start_day)

li = []
while True:
    start_date += datetime.timedelta(1)
    s = str(start_date)
    tmp = s[: 4] + s[5: 7] + s[8:]
    if tmp == tmp[::-1]:
        li.append(int(tmp))
        if tmp[0] == tmp[2] == tmp[5] == tmp[7] and tmp[1] == tmp[3] == tmp[4] == tmp[6]:
            end = int(tmp)
            break
print(li[0])
print(end)
