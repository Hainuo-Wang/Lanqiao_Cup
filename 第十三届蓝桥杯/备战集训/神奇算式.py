''''''
'''
由4个不同的数字，组成的一个乘法算式，它们的乘积仍然由这4个数字组成。比如:
210 x 6 = 1260 
8 x 473 = 3784
27 x 81 = 2187 
都符合要求。
如果满足乘法交换律的算式算作同一种情况，那么，包含上边已列出的3种情况，一共有多少种满足要求的算式。
'''
'''
1、审题：遇到这种数论题，一定要细心，挖掘出题目中所有的隐藏条件。
条件1：“4个不同数字”。(set去重)
条件2：“满足乘法交换律的算式算作同一种情况”。(小×大)
条件n：······
2、建模：思考自己的手上有哪些函数，可以高效快捷地搭建模型，解决问题。
★★★ 比如数论常考的函数：str()  list()  sorted()  set()  len() ★★★
3、解题：
因为算式左边的数字很小，最大只有一千，所以我们选择二层循环遍历每种情况。
第一步遍历了所有情况，接下来就是★★★按照条件筛选★★★了。
把手里的工具组合起来，整数int转换成字符串str()，字符串转换成字符列表list()
再排个序sorted() 这个时候范围已经缩小了很多。
接下来继续筛选，打印现在的输出 print(i,j,i*j) ，看看哪些不符合条件。
测试输出：750*906=679500，确实有4个不同数字，但跟题目给的样例差距太大了。
所以我们可以看出还有隐藏条件需要挖掘，再进行筛选，加个if判断。
750*906 不能重复set()， 并且长度应该是4，所以要满足len(set(s))==len(set(t))==4
观察i*j=679500,发现数值超过范围10000，所以需要增加数字范围约束1000<i*j<9999
'''
num = 0
for i in range(1, 1000):
    for j in range(i + 1, 1000):  # 小×大
        product = i * j
        len_product = len(str(product))  # 长度为4
        len_set_product = len(set(str(product)))  # 长度也要为4
        len_i = len(str(i))
        len_j = len(str(j))
        len_ij = len_j + len_i  # 长度为4
        len_set_ij = len(set(str(i) + str(j)))  # 长度也要为4
        set_product = sorted(list(str(product)))
        set_ij = sorted(list(str(i) + str(j)))
        if len_ij == len_set_ij == len_product == len_set_product == 4 and set_product == set_ij:
            # print('{}*{}={}'.format(i, j, product))
            num += 1
print(num)
