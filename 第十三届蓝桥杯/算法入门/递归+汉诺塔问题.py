'''递归问题'''

'''
递归的两个特点：
调用自身
结束条件
'''
def Hanoi(n, a, b, c):  # 将n个盘子从a经过b移动到c
    if n > 0:
        Hanoi(n - 1, a, c, b)
        print('move from %s to %s' % (a, c))
        Hanoi(n - 1, b, a, c)
    '''
    h(x) = 2h(x - 1) + 1
    '''

Hanoi(3, 'A', 'B', 'C')
'''
汉诺塔问题：A、B、C三根柱子，A柱子从上到下串着从小到大的n个圆盘，欲将这n个圆盘全部移动到另外的一根柱子上，且移动过程中，大的圆盘不能放在小的
          圆盘上，问需要移动多少次？
          
          假设只有2个圆盘的情况下，第一步A->B，
                               第二步A->C，
                               第三步B->C，共移动3次。
          
          假设只有3个圆盘的情况下，第一步A->C，
                               第二步A->B，
                               第三步C->B，
                               第四步A->C，
                               第五步B->A，
                               第六步B->C，
                               第七步A->C，共需要移动7次。
          其中前三步相当于上面的2个圆盘经过C整体移动到了B，相当于只有2个圆盘时的第一步；
          第四步直接将最大的圆盘从A移动到C，相当于只有2个圆盘时的第二步；
          后三步相当于将B上面2个圆盘整体的经过A移动到了C，相当于只有2个圆盘时的第三步。
          
          则当n>3时，可以将上面的n-1个圆盘看成一个整体，第一步整体从A经过C移动到B，
                                                 第二步大圆盘从A直接移动到C，
                                                 第三步整体从B经过A移动到C。
'''

def Hanoi(n, a, b, c):  # 将n个盘子从a经过b移动到c
    if n > 0:
        Hanoi(n - 1, a, c, b)
        print('move from %s to %s' % (a, c))
        Hanoi(n - 1, b, a, c)
    '''
    h(x) = 2h(x - 1) + 1
    '''

Hanoi(3, 'A', 'B', 'C')