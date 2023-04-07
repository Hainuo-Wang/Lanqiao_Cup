# 问题描述
#
# 如果一个自然数N的K进制表示中任意的相邻的两位都不是相邻的数字，那么我们就说这个数是K好数。求L位K进制数中K好数的数目。例如K = 4，L = 2的时候，所有K好数为11、13、20、22、30、31、33 共7个。由于这个数目很大，请你输出它对1000000007取模后的值。
# 输入格式
#
# 输入包含两个正整数，K和L。
# 输出格式
# 输出一个整数，表示答案对1000000007取模后的值。
# 样例输入
# 4 2
# 样例输出
# 7
# 数据规模与约定
#
# 对于30%的数据，KL <= 106；
#
# 对于50%的数据，K <= 16， L <= 10；
#
# 对于100%的数据，1 <= K,L <= 100。
#
# 动态规划DP问题
# “L位K进制数”：如：“2位4进制数”，它是指这个数是个两位数，其中个位数是4进制数（即从[0,3]中取一个数作为个位），十位数也是4进制数。同理，“3位7进制数”则指这个数是个3位数，其中个位、十位、百位都是7进制数。
# K好数的要求：任意相邻的两位不是相邻的数字。
# 核心：dp[i][j]=dp[i][j]+dp[i-1][k]
# 当前位置的数总数=当前位置的数的数目+前一个位置的数的总数。
def count(length, kind, ans):
    for i in range(1, kind):
        dp[0][i] = 1
    for i in range(1, length):
        for j in range(kind):
            for k in range(kind):
                if abs(j - k) != 1:
                    if j - 1 == 0 and k == 0:  # 排除首位为0的情况
                        continue
                    dp[i][j] = dp[i][j]+dp[i-1][k]
                    dp[i][j] %= MOD
    for i in range(kind):
        ans += dp[length - 1][i]
        ans %= MOD
    return ans


K, L = map(int, input().split())

ans = 0

MOD = 1000000007

dp = [[0 for _ in range(max(L,K))] for _ in range(max(L,K))]

if K == 1 and L == 1:
    print(0)
elif K > 1 and L == 1:  # 1位的K进制的K好数总数就是K个
    print(K)
elif L > 1:
    print(count(L, K, ans))



