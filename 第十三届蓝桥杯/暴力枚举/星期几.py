''''''
import datetime

'''
题目描述:
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
1949年的国庆节（10月1日）是星期六。
今年(2012)的国庆节是星期一。
那么，从建国到现在，有几次国庆节正好是星期日呢?不要求写出具体是哪些年，只要一个数目!
'''

start = datetime.date(1949, 10, 1)
end = datetime.date(2012, 10, 1)
counter = 0
while start < end:
    if start.weekday() == 6 and start.month == 10 and start.day == 1:
        counter += 1
    start += datetime.timedelta(1)
print(counter)