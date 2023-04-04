# 问题描述
# 　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
# 　　例如：
# 　　A =
# 　　1 2
# 　　3 4
# 　　A的2次幂
# 　　7 10
# 　　15 22
# 输入格式
# 　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
# 　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值
# 输出格式
# 　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。
# 相邻的数之间用一个空格隔开
# 样例输入
# 2 2
# 1 2
# 3 4
# 样例输出
# 7 10
# 15 22
#
# 注意：
#
# 1.不要忘记方阵的0次幂这一特殊情况，它的结果是人为定义的，为n阶单位阵。
# 2.博主的代码中矩阵乘法函数，是一个普遍适用的矩阵乘法函数，
# 即不是两个方阵相乘也行，只要两矩阵满足矩阵乘法定理即可，相应解释已在代码块中给出。
# 3.若你在参加考试，则代码越简化越好，如这题的矩阵乘法函数，
# 题中给的输入矩阵必为n阶方阵，所以写矩阵乘法的函数就只针对n阶方阵来写就好了，
# 以降低出错率，相应代码请读者自行写出，以加深理解。
def multi_rect(rect_1, shape_1, rect_2, shape_2):
    """
    :param rect_1: 矩阵A
    :param shape_1: 矩阵A的形状
    :param rect_2: 矩阵B
    :param shape_2: 矩阵B的形状
    :return: 两矩阵之积和积的矩阵形状
    """
    if shape_1[1] != shape_2[0]:
        return
    rect_ = [[0 for _ in range(shape_2[1])] for _ in range(shape_1[0])]
    shape_ = (shape_1[0], shape_2[1])
    for i in range(shape_1[0]):
        for k in range(shape_2[1]):
            for j in range(shape_1[1]):
                rect_[i][k] += rect_1[i][j] * rect_2[j][k]  # 矩阵乘法定义
    return rect_, shape_


n, m = map(int, input().split())
rect = [[] for _ in range(n)]
for i in range(n):
    arr = input().split()
    for j in range(n):
        rect[i].append(int(arr[j]))
result, shape = rect, (n, n)
if m == 0:
    result = [[0 for _ in range(n)] for _ in range(n)]
else:  # m不为0，计算它的m次幂
    for _ in range(m - 1):
        result, shape = multi_rect(rect, (n, n), result, shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        print(result[i][j], end=' ')
    print()




