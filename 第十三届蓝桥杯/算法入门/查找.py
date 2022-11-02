from Calculate_Time import *

'''
查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程。

列表查找（线性表查找）：从列表中查找指定元素。
输入：列表和待查找元素
输出：元素下标（未找到元素返回None或者-1）

内置列表查找函数：index()
'''

'''
顺序查找（Linear Search）：也叫线性查找，从线性表（Linear list）第一个元素开始，顺序进行搜索，直到找到元素或者搜索到列表最后一个元素为止。
时间复杂度为：O(n)
'''
@Cal_Ti
def Linear_Search(li, val):
    for idx, v in enumerate(li):
        if v == val:
            return idx
    else:
        return None

li = list(range(10000))
print('Linear Search: index = {}'.format(Linear_Search(li, 6588)))

'''
二分查找：又叫折半查找，从有序列表（Sequence List）的初始候选区li[0:n]开始，通过对待查找的值与候选区的中间值进行比较，可以使候选区减少一半。
时间复杂度为：O(logn)
'''
@Cal_Ti
def Binary_Search(seq, val):
    left = 0  # 候选区第一个数
    right = len(seq) - 1  # 候选区最后一个数
    while left <= right:  # 只要候选区有值，就接着进行搜索
        middle = (left + right) // 2
        if seq[middle] == val:
            return middle
        elif seq[middle] > val:
            right = middle - 1
        else:  # seq[middle] < val
            left = middle + 1
    else:
        return None

print('Binary Search: index = {}'.format(Binary_Search(li, 6588)))