''''''
'''
题目描述:
本题为填空题，只需要算出结果后，在代码中使用输出语句将所填结果输出即可。
把1~9这9个数字分成2组，中间插入乘号，有的时候，它们的乘积也只包含1~9这9个数字，而且每个数字只出现1次。
比如:
984672 * 351 = 345619872
98751 * 3462 = 341875962
9 * 87146325 = 784316925
...
符合这种规律的算式还有很多，请你计算在所有这些算式中，乘积最大是多少?
注意，需要输出的是一个整数，表示那个最大的积，只输出乘积，不要输出整个算式。
'''
from itertools import permutations
li = set()
for case in permutations('123456789'):
    tmp = ''.join(case)
    for idx in range(1, 9):  # [1, 8]
        multiple = int(tmp[: idx]) * int(tmp[idx:])
        if len(set(str(multiple))) == 9 and '0' not in str(multiple):
            li.add(multiple)
print(max(li))  # 839542176
