# 要在n*n的国际象棋棋盘中放n个皇后，使任意两个皇后都不能互相吃掉。
# 规则：皇后能吃掉同一行、同一列、同一对角线的任意棋子。求所有的解。
# n=8是就是著名的八皇后问题了。
n = 0  # 记录有多少种放法
def dfs(num, res, row):  # 参数：皇后总数  位置总结果  当前放置第几行
    global n
    # 如果当前行数 = 皇后总数，结束跳出
    if row == num:
        print(res)
        n += 1
        return
    # 遍历 row 行中的每一列，判断是否可行
    for col in range(num):
        if check(col, res, row):  # 若可行
            res[row] = col   # 将该 row 行的数值改成列数 col
            dfs(num, res, row + 1)   # 进行下一行的搜索
            # 若进行到这一步说明，上一步走后，后续无法再放置皇后，需要回溯
            # 也可以不回溯，因为进入下一个循环（将该 row 行的数值改成列数 col + 1）后，会重新对 res[row] 赋值
            res[row] = 0


def check(col, res, row):  # 参数：当前列  位置总结果  当前行
    # 遍历已经放好皇后的所有行（不用判断是否在同一行，因为一行有值后，会进行到下一个 dfs）
    for i in range(row):
        # 1、是否在同一列中    2、左斜线：（行 + 列）的值相等    3、右斜线：（列 - 行）的值相等
        if res[i] == col or res[i] + i == row + col or res[i] - i == col - row:
            return False
    return True


if __name__ == '__main__':
    # num: 皇后的数量
    num = int(input('请输入皇后的数量：'))
    # 最终皇后的位置 （下标：第几行 数值：第几列）
    res = [0 for _ in range(num)]
    # 从第一行开始
    row = 0
    # 参数：皇后总数  位置结果  当前放置第几行
    dfs(num, res, row)
    print(n)
