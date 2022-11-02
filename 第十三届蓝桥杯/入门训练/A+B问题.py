''''''
'''
输入A、B，输出A+B

输入格式:
输入的第一行包括两个整数，由空格分隔，分别表示A、B
'''

A, B = map(int, input().split())
print(A + B)

'''
map(function, iterable, ...)函数，参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
'''

'''
str.split()函数，默认以空格为分隔符对str进行分割，返回分割后的列表。
'''