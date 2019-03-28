# -*- coding: utf-8 -*-
"""

# 题

同样凭记忆回忆一下, 从原点出发, 输入5个节点的坐标, 然后找从原点出发经过每个点回到原点的最短路径.

# 输入

输入5个坐标的位置, 用空格分割

# 思路

因为最短路径是一个NP问题, 当时考虑不知道怎么求解, 粗略写了一个贪心求解策略, 考虑如果是凸函数的话, 贪心是可以求解的. 但代码可能还存在很多问题, 实际存在很多问题罢.

但事后和室友说起来, 室友说既然指定了5个点, 那么直接暴力遍历写一个五层循环即可.


"""
import re
import math

# 本来想每个点可以用几种方法的, 但后来觉得太麻烦, 因此这个类比较冗余
class point:
    x = int()
    y = int()
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 求两点距离
def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# 输入
ipt = input()

# 对输入做一个正则分割, 因为python没有好的格式化输入的解析
s = ''.join(ipt)
result = re.findall(r"(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)\s(.+)", s)
if not result:
    print("parse failed")
    exit(1)
content = result[0]

# 存储点
points = list()
points.append(point(0,0))
for i in range(5):
    p = point(int(content[2*i]), int(content[2*i+1]))
    points.append(p)


num = len(points)
solution = 0

# 对每个点求最短距离
for i in range(num-1):
    shortest = 1000000000000
    for j in range(i+1, num):
        dis = distance(points[i], points[j])
        if dis < shortest:
            shortest = dis
    solution += shortest

d2 = distance(points[num-1], point(0.0,0.0))

solution += d2

print(math.floor(solution))
