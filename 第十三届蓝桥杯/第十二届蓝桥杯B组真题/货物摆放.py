''''''
'''
小蓝有一个超大的仓库，可以摆放很多货物。
现在，小蓝有n箱货物要摆放在仓库，每箱货物都是规则的正方体。小蓝规定了长、宽、高三个互相垂直的方向，每箱货物的边都必须严格平行于长、宽、高。
小蓝希望所有的货物最终摆成一个大的立方体。即在长、宽、高的方向上分别堆L、W、H的货物，满足n=Lx wx H。
给定n，请问有多少种堆放货物的方案满足要求。
例如，当n = 4时，有以下6种方案:1×1×4、1×2×2、1×4×1、2×1×2、2×2×1、4×1×1。
请问，当n = 2021041820210418（注意有16位数字）时，总共有多少种方案?
'''
n = int(input())
divisors = set()  # 约数集合去重
cases = 0
for i in range(1, int(n**0.5) + 1):  # 根号n
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)
for l in divisors:
    for w in divisors:
        for h in divisors:
            if l * w * h == n:
                cases += 1
print(cases)
