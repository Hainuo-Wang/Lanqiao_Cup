''''''
'''
题目描述
Huffman树在编码中有着广泛的应用。在这里，我们只关心Huffman树的构造过程。
给出一列数{pi}={p0, p1, …, pn-1}，用这列数构造Huffman树的过程如下：
找到{pi}中最小的两个数，设为pa和pb，将pa和pb从{pi}中删除掉，然后将它们的和加入到{pi}中。这个过程的费用记为pa + pb。
重复步骤1，直到{pi}中只剩下一个数。
在上面的操作过程中，把所有的费用相加，就得到了构造Huffman树的总费用。
本题任务：对于给定的一个数列，现在请你求出用该数列构造Huffman树的总费用。
例如，对于数列{pi}={5, 3, 8, 2, 9}，Huffman树的构造过程如下：
找到{5, 3, 8, 2, 9}中最小的两个数，分别是2和3，从{pi}中删除它们并将和5加入，得到{5, 8, 9, 5}，费用为5。
找到{5, 8, 9, 5}中最小的两个数，分别是5和5，从{pi}中删除它们并将和10加入，得到{8, 9, 10}，费用为10。
找到{8, 9, 10}中最小的两个数，分别是8和9，从{pi}中删除它们并将和17加入，得到{10, 17}，费用为17。
找到{10, 17}中最小的两个数，分别是10和17，从{pi}中删除它们并将和27加入，得到{27}，费用为27。
现在，数列中只剩下一个数27，构造过程结束，总费用为5+10+17+27=59。
输入:
输入的第一行包含一个正整数n（n< =100）。
接下来是n个正整数，表示p0, p1, …, pn-1，每个数不超过1000。
输出:
输出用这些数构造Huffman树的总费用。
'''
n = int(input())
li = list(map(int, input().split()))

def Bubble_Sort(li):
    for i in range(len(li) - 1):
        Whether_Exchange = False
        for j in range(len(li) - i - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                Whether_Exchange = True
        if not Whether_Exchange:
            return
cost = 0
while len(li) != 1:
    Bubble_Sort(li)
    n_1 = li.pop()
    n_2 = li.pop()
    s = n_1 + n_2
    li.append(s)
    cost += s
print(cost)

'''
def Improved_Bubble_Sort(li):  # 从后往前升序冒泡，可以较大程度的减少迭代次数
    for i in range(len(li) - 1):
        Whether_Exchange = False
        for j in range(len(li) - 1, i, -1):
            if li[j] > li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
                Whether_Exchange = True
        if not Whether_Exchange:
            return
'''