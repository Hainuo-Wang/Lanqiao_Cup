# 一个字符串的非空子串是指字符串中长度至少为
# 1
# 的连续的一段字符组成
# 的串。例如，字符串aaab
# 有非空子串a, b, aa, ab, aaa, aab, aaab，一共
# 7
# 个。 注意在计算时，只算本质不同的串的个数。
#
# 请问，字符串0100110001010001
# 有多少个不同的非空子串？
var = '0100110001010001' # var = 'aaab' 运行结果为7 表示算法正确
num = 1 # 自身也是1个，循环中没有去考虑他串本身，所以这里基数直接设置为1
sep = 1
var_n = []
while sep < len(var):
    var_n.append(var[0:sep])
    for i in range(len(var)-sep):  # 以sep为间隔依次向前推进，sep每轮循环增1
        if var[i+1:i+sep+1] in var_n:
            continue
        else:
            var_n.append(var[i+1:i+sep+1])
    sep += 1
    num += len(var_n)
    # print(var_n)
    var_n = []
print(num)

