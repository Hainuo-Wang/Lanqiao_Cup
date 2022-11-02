''''''
'''
在平面直角坐标系中，两点可以确定一条直线。如果有多点在一条直线上，那么这些点中任意两点确定的直线是同一条。
给定平面上2 × 3个整点{(x, y)|0 ≤ x < 2, 0 ≤ y < 3,x ∈ Z, y ∈ Z)，即横坐标是О到1(包含0和1)之间的整数、
纵坐标是О到2(包含О和2)之间的整数的点。这些点一共确定了11条不同的直线。
给定平面上20 × 21个整点{(x,y)|0 ≤ x < 20, 0 ≤ y < 21,x ∈ Z,y ∈ Z)，即横坐标是0到19(包含О和19)之间的整数、
纵坐标是О到20(包含0和20)之间的整数的点。请问这些点一共确定了多少条不同的直线。
'''
'''
思路：（斜率，截距）来区分，集合去重
'''
import time
start = time.perf_counter()
points = [(x, y) for x in range(20) for y in range(21)]
docker = set()
for point_1 in points:
    x_1, y_1 = point_1
    for point_2 in points:
        x_2, y_2 = point_2
        if x_1 == x_2 or y_1 == y_2:  # 跳过斜率不存在和斜率等于0的情况
            continue
        k = (y_2 - y_1) / (x_2 - x_1)
        b = (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1)
        docker.add((k, b))
end = time.perf_counter()
print(len(docker) + 41)
print('Running time: ', end - start)