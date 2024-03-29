# 问题描述：
# 　　生理卫生老师在课堂上娓娓道来：
# 　　你能看见你未来的样子吗？显然不能。但你能预测自己成年后的身高，有公式：
# 　　男孩成人后身高=（父亲身高+母亲身高）/21.08
# 　　女孩成人后身高=(父亲身高0.923+母亲身高）/2
# 　　数学老师听见了，回头说：这是大样本统计拟合公式，准确性不错。
# 　　生物老师听见了，回头说：结果不是绝对的，影响身高的因素很多，比如营养、疾病、体育锻炼、睡眠、情绪、环境因素等。
# 　　老师们齐回头，看见同学们都正在预测自己的身高。
# 　　毛老师见此情形，推推眼镜说：何必手算，编程又快又简单…
# 　　约定：
# 　　身高的单位用米表示，所以自然是会有小数的。
# 　　男性用整数1表示，女性用整数0表示。
# 　　预测的身高保留三位小数
# 输入格式
# 　　用空格分开的三个数，整数 小数 小数
# 　　分别表示：性别 父亲身高 母亲身高
# 输出格式
# 　　一个小数，表示根据上述表示预测的身高（保留三位小数）
# 样例输入
# 1 1.91 1.70
# 样例输出
# 1.949
# 样例输入
# 0 1.00 2.077
# 样例输出
# 1.500
# 数据规模和约定
# 　　父母身高范围（0，3]
# 　　时间限制1.0秒
gender, father_height, mother_height = map(float, input().split())

if gender == 1:
    height = (father_height + mother_height) / 2 * 1.08
else:
    height = (father_height * 0.923 + mother_height) / 2

print('%.3f' % height)


