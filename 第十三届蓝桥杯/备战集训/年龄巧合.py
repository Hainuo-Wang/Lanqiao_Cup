''''''
'''
填空题：
小明和他的表弟一起去看电影，有人问他们的年龄。小明说：今年是我的幸运年，我出生年份的四位数字加起来刚好是我的年龄。
表弟的也是如此。已知今年是 2014 年，并且，小明说的年龄指的是周岁。
请推断并填写出小明和他表弟的出生年份。
'''
import time
start = time.perf_counter()
year = 2014
count = 0
while True:
    year -= 1
    if 2014 - year == int(str(year)[0]) + int(str(year)[1]) + int(str(year)[2]) + int(str(year)[3]):
        count += 1
        print(year)
    if count == 2:
        break
end = time.perf_counter()
print('Running time: ', end - start)