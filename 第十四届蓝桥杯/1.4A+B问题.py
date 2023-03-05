# 问题描述
#
# 输入A、B，输出A+B。
#
# 输入格式
#
# 输入的第一行包括两个整数，由空格分隔，分别表示A、B。
#
# 输出格式
#
# 输出一行，包括一个整数，表示A+B的值。
#
# 样例输入
#
# 12 45
#
# 样例输出
#
# 57
#
# 数据规模与约定
#
# -10000 <= A, B <= 10000
# a, b = map(int, input().split())
# print(a + b)


# 大数加法

def big_data_add(a, b):
    # 1.先获取两个中最大的长度，然后将短进行补充，使长度一致
    max_len = len(a) if len(a) > len(b) else len(b)

    a = a.zfill(max_len)
    b = b.zfill(max_len)
    # 输出看看  我们发现长度一致
    # print(a)
    # print(b)
    a = list(a)
    b = list(b)
    result = [0 for i in range(max_len + 1)]  # 这里加1主要是考虑到两数加起来可能比之前的数还多一位

    for i in range(max_len - 1, -1, -1):
        temp = int(a[i]) + int(b[i])
        if temp >= 10:
            # 这里result是i+1  是因为result的长度比max_len长度长
            result[i + 1] += temp % 10
            result[i] += temp // 10
        else:
            result[i + 1] += temp

    return result


if __name__ == '__main__':
    # 首先定义了两个数  用字符串给出
    a = '543425435465473423038950284590702985902890670982032850808403649038502802859285249045'
    b = '890795609630592689208605865987690876939065989028928905820685208609820695'
    c = ''
    result = big_data_add(a, b)
    for i in range(0, len(result)):
        c += str(result[i])
    if c[len(c) - 1] == '0':
        c = c[1:len(c)]
    print('{}\n + {} \n = {}'.format(a, b, c))

