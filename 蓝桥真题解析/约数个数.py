"""
【问题描述】
1200000有多少个约数（只计算正约数）。
【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""
count = 2
for i in range(2, 1200000):
    if 1200000 % i == 0:
        count += 1
        # print(i)
print(count)