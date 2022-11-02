''''''
import datetime

'''
题目描述:
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
小蓝特别喜欢2，今年是公元2020年，他特别高兴，因为每天日历上都可以看到2
如果日历中只显示年月日，请问从公元1900年1月1日到公元9999年12月31日，一共有多少天日历上包含2。即有多少天中年月日的数位中包含数字2。
'''
counter = 0
start = datetime.date(1900, 1, 1)  # 蓝桥杯中一定要导入datetime包
end = datetime.date(9999, 12, 31)
while start < end:  # 不能写成start <= end，因为这样，最后一次，将超出四位数年数，报错
    if '2' in str(start):
        counter += 1
    start += datetime.timedelta(1)
print(counter + 1)  # 1994240
