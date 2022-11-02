''''''
'''
题目:
今盒子里有 n 个小球，A、B 两人轮流从盒中取球，每个人都可以看到另一个人取了多少个，也可以看到盒中还剩下多少个，并且两人都很聪明，不会做出错误的判断。
我们约定：
每个人从盒子中取出的球的数目必须是：1，3，7 或者 8 个。轮到某一方取球时不能弃权！
A 先取球，然后双方交替取球，直到取完。被迫拿到最后一个球的一方为负方（输方）.
请编程确定出在双方都不判断失误的情况下，
输入描述:
先是一个整数 n(n<100)，表示接下来有 n 个整数。
然后是 n 个整数，每个占一行（整数< 10^4），表示初始球数。
输出描述
程序则输出 n 行，表示 A 的输赢情况（输为 0，赢为 1）。
样例输入:
4
1
2
10
18
样例输出:
0
1
1
0
'''
'''
分析：当只有1个球的时候，A摸，输掉比赛，当增加1，3，7，8个球时，A赢得比赛。
     初始化所有局A都输掉，全部为0，且dp[1]一定为0，从dp[1]开始遍历，碰到A输掉的情况，那么，增加1，3，7，8个球，A就会赢。
'''
dp = [0] * 10000  # 最多9999个球，索引为0不考虑，dp[i]为初始为i个球时A的输赢情况
n = int(input())  # 共n轮
for epoch in range(n):
    initial_num = int(input())
    for i in range(1, initial_num + 1):  # 从初始状态只有1个球开始遍历，且dp[1]==0
        if dp[i] == 0:  # 当A会输时，增加1，3，7，8个球，A就会赢
            dp[i + 1] = dp[i + 3] = dp[i + 7] = dp[i + 8] = 1
    print(dp[initial_num])




