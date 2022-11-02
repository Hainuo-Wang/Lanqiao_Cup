''''''
'''
贪心算法(Greedy Algorithm)含义:
在对问题求解时，总是作出在当前看来是最好的选择。也就是说，不从整体上加以考虑，它所作出的仅仅是在某种意义上的局部最优解（是否是全局最优，需要证明）。
'''

'''
最优装载问题:
有一天海盗们截获了一艘装满各种各样古董的货船，每一件都价值连城，一旦打碎就是去了价值， 海盗船载重量为C，每件固定的重量为w[i]，
海盗们该如何尽可能装载最多数量的古董呢？ 
古董重量清单:
重量W[i]:4 10 7 11 3 5 14 2
算法设计:
船载重量固定为C，要求尽可能多装载，只要每次选择重量最小的古董，直到不能再装为止，这样装载的古董数量最大，这就是贪心策略
'''
# weight = [4, 10, 7, 11, 3, 5, 14, 2]
# weight_sorted = sorted(weight)
# c = int(input('海盗船装载最大重量为:'))
# num, current_weight = 0, 0
# load = []
# for elem in weight_sorted:
#     current_weight += elem
#     if current_weight <= c:
#         num += 1
#         load.append(elem)
# print('可装载的古董数量为:', num)
# print('装载的几个古董的重量为:', load)

'''
背包问题:
假设山洞中有n种宝物，每种宝物有一定重量w和相应的价值v，毛驴运载能力为一种宝物只能拿一样，宝物可分割。怎样才能使毛驴运走宝物的价值最大呢？
可以尝试三种贪心策略:
每次挑选价值最大的装入背包；
每次挑选最重的东西；
每次选取单位重量价值（性价比）最大的东西。
根据贪心策略，按性价比从大到小选取宝物，直到达到毛驴的运载能力。每次选择宝物后判断是否小于m，如果不小于则取走宝物的一部分，程序结束。
'''
# datas = [[4, 3], [2, 8], [9, 18], [5, 6], [5, 8], [8, 20], [5, 5], [4, 6], [5, 7], [5, 15]]
# # datas中每一行代表一个古董，每一行第一个元素代表古董重量，第二个元素代表古董价值
# donkey = 30  # 毛驴的运载能力
# total_value = 0
# for i in range(len(datas)):
#     cost_performance = datas[i][1] / datas[i][0]  # 性价比
#     datas[i].append(cost_performance)
# datas.sort(key=lambda data: data[2], reverse=True)  # 按照性价比降序
# for data in datas:
#     if data[0] <= donkey:
#         total_value += data[1]
#         donkey -= data[0]
#     else:  # 此时毛驴剩余的装载量小于该古董的重量，只能拿走一部分
#         total_value += data[2] * donkey  # 用剩余装载量乘以该古董的性价比就是该部分的价值
#         break
# print(total_value)

'''
分糖果:已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，当某个糖果的大小s>=某个孩子的需求因子g时，代表该糖果可以满足该孩子，
求使用这些糖果，最多能满足多少孩子（注意，某个孩子最多只能用1个糖果满足）
'''
# def Most_Satisfy(g, s):
#     '''
#     :param g: len(g)为孩子的数量
#     :param s: len(s)为糖果的数量
#     :return:
#     '''
#     g, s = sorted(g), sorted(s)
#     child_num, candy_num = len(g), len(s)
#     satisfied_child = 0
#     distributed_candy = 0
#     while satisfied_child < child_num and distributed_candy < candy_num:
#         if g[satisfied_child] <= s[distributed_candy]:
#             satisfied_child += 1
#         distributed_candy += 1
#     return satisfied_child
#
# g = [5, 10, 2, 9, 15, 9]
# s = [6, 1, 20, 3, 8]
# print(Most_Satisfy(g, s))

'''
一辆汽车加满油后可行驶n公里。旅途中有若干个加油站。设计一个有效算法，指出应在哪些加油站停靠加油，使沿途加油次数最少。
对于给定的n(n <= 5000)和k(k <= 1000)个加油站位置，编程计算最少加油次数。
'''
# def Least_Refuel(dis, sta_num, dis_li):
#     '''
#     :param dis: 加满油可行驶dis公里
#     :param sta_num: 加油站个数
#     :param dis_li: 汽车到第一个加油站的距离，两个加油站之间的距离，最后一个加油站到终点的距离
#     :return: None
#     '''
#     num = 0  # 加油次数
#     # 先测试汽车在加满油后，是否可以到达下一个加油站，或者到达终点
#     for d in dis_li:
#         if d > dis:
#             print('No solution!')
#             return
#     i = 0  # 经过加油站个数
#     d = 0  # 加满油后行驶公里数
#     while i <= sta_num:
#         d += dis_li[i]
#         if d > dis:  # 到不了第i个加油站
#             num += 1  # 在第i-1个加油站加满油
#             d = dis_li[i]  # 在第i-1个加油站加满油，还要行驶distance[i]的路程
#         i += 1
#     print(num)
#
# Least_Refuel(100, 5, [50, 80, 39, 60, 40, 32])

'''
求最大子数组之和问题：给定一个整数数组（数组元素有负有正），求其连续子数组之和的最大值
'''
# def Max_Subarray_Sum(li):
#     li_max, li_sum = 0, 0
#     for i in range(len(li)):  # 从第一个数开始看
#         li_sum += li[i]
#         if li_sum > li_max:  # 从前往后加，若和大于当前最大值，就更新最大值
#             li_max = li_sum
#         elif li_sum < 0:  # 若和小于零，就从下一位重新开始加
#             li_sum = 0
#     print(li_max)
#
# Max_Subarray_Sum([12, -4, 32, -36, 12, 6, -6])

'''
找零钱问题:
假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1元的硬币。在超市结账 时，如果 需要找零钱， 收银员希望将最少的硬币数找给顾客。
那么，给定 需要找的零钱数目，如何求得最少的硬币数呢？
'''
def Least_Coin(num):
    coin_li = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    total_coin_num = []
    coin_sum = 0
    num_li = [0] * len(coin_li)

    for idx, i in enumerate(input('拥有每种硬币的个数:').split()):
        total_coin_num.append(int(i))
        coin_sum += int(i) * coin_li[idx]

    if num > coin_sum:
        print('No solution!')
        return
    i = 6
    while i >= 0:
        if num >= coin_li[i]:
            n = int(num / coin_li[i])
            if n >= total_coin_num[i]:
                n = total_coin_num[i]
            num_li[i] = n
            num -= n * coin_li[i]
            num = round(num, 2)  # 保留两位小数
            if num == 0:
                break
        i -= 1
    else:
        if num != 0:
            print('Can not change!')
            return
    print(num_li)
    return
Least_Coin(5.25)
