''''''
'''
题目描述:
小蓝正在学习一门神奇的语言，这门语言中的单词都是由小写英文字母组成，有些单词很长，远远超过正常英文单词的长度。
小蓝学了很长时间也记不住一些单词，他准备不再完全记忆这些单词，而是根据单词中哪个字母出现得最多来分辨单词。
现在，请你帮助小蓝，给了一个单词后，帮助他找到出现最多的字母和这个字母出现的次数。
输入描述:
输入一行包含一个单词，单词只由小写英文字母组成。对于所有的评测用例，输入的单词长度不超过1000。
输出描述:
输出两行，第一行包含一个英文字母，表示单词中出现得最多的字母是哪个。如果有多个字母出现的次数相等，输出字典序最小的那个。
第二行包含一个整数，表示出现得最多的那个字母在单词中出现的次数。
'''
word = sorted(list(input()))
print(word)
alphabet = sorted(word, key=lambda x: word.count(x), reverse=True)[0]
print(sorted(word, key=lambda x: word.count(x), reverse=True))
print(alphabet)
print(word.count(alphabet))
'''
word = list(input())
word_set = sorted(set(word))
alphabet_num_li = []
for alphabet in word_set:
    alphabet_num_li.append(word.count(alphabet))
idx = alphabet_num_li.index(max(alphabet_num_li))
print(word_set[idx])
print(alphabet_num_li[idx])
'''