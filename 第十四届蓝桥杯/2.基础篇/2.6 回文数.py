# 正着数和倒着数都一样，输出所有的这样的四位数
# 如 1221

def is_pal(i_):
    i_s = str(i_)  # 转为字符串，可倒置
    if i_s == i_s[::-1]:
        return True
    else:
        return False


i = 1000
while i < 10000:
    if is_pal(i):
        print(i)
    i += 1

