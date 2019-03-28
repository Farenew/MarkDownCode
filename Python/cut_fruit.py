# -*- coding: utf-8 -*-
"""

# 题

凭记忆回忆一下题, 大意是给出一个40*50的矩阵, 里面每一个点都可以放一个水果. 现在要求使用最少的切法把所有的水果都切到. 可以横着切, 可以竖着切, 可以对角线斜着切.

简化的示例:

0 1 0
0 1 0
0 0 1

这样的结构需要至少两次切割.

# 输入

首先输入一个数字, 说明接下来要输入几个水果的位置.

实例:

2
1 3
2 4

# 思路

时间所限, 直接暴力求解, 对每个位置判断, 找出来一次切割能切到最多的水果方案. 直到水果的数量减到0.

# 函数简介

- get_fruits(ar,xlim, ylim, x,y,type = "row"), 判断当前位置某个切割方法能切到最多的水果数量
- cut_fruit(ar,xlim, ylim, x,y,type), 切割水果.


"""
import numpy as np

def get_fruits(ar,xlim, ylim, x,y,type = "row"):
    sum = 0
    if type == "row":
        for i in range(xlim):
            sum += ar[i,y]
        return sum
    if type == "column":
        for i in range(ylim):
            sum += ar[x, i]
        return sum
    if type == "diagonal":
        i = x
        j = y
        while i<xlim and j<ylim:
            sum += ar[i,j]
            i += 1
            j += 1
        i = x
        j = y
        while i>=0 and j>=0:
            sum += ar[i, j]
            i -= 1
            j -= 1
        return sum - ar[x,y]
    if type == "anti-diagonal":
        i = x
        j = y
        while i >= 0 and j < ylim:
            sum += ar[i, j]
            i -= 1
            j += 1
        i = x
        j = y
        while i < xlim and j >= 0:
            sum += ar[i, j]
            i += 1
            j -= 1
        return sum - ar[x,y]

def cut_fruit(ar,xlim, ylim, x,y,type):
    sum = 0
    if type == 1:
        for i in range(xlim):
            ar[i,y] = 0
    if type == 2:
        for i in range(ylim):
            ar[x, i] = 0
    if type == 3:
        i = x
        j = y
        while i<xlim and j<ylim:
            ar[i,j] = 0
            i += 1
            j += 1
        i = x
        j = y
        while i>0 and j>0:
            ar[i, j] = 0
            i += 1
            j += 1
    if type == 4:
        i = x
        j = y
        while i < xlim and j < ylim:
            ar[i, j] = 0
            i -= 1
            j += 1
        i = x
        j = y
        while i > 0 and j > 0:
            ar[i, j] = 0
            i += 1
            j -= 1

def main():
    # 初始化水果矩阵
    ar = np.full([40,50],0, dtype=int)

    # num是输入, 也表示了水果数量
    num = input()

    # 输入水果
    for i in range(int(num)):
        s = input()
        a, b = [int(i) for i in s.split(' ')]
        ar[a,b] = 1

    # 这次遍历中能实现的最大切割
    mostEli = 0
    # 剩下的水果数量
    remain = int(num)
    # 最大切割时的切割位置
    max_x = 0
    max_y = 0
    # 切割次数
    cut_num = 0

    while remain != 0:
        for i in range(40):
            for j in range(50):
                row = get_fruits(ar, 40, 50, i, j, type="row")
                column = get_fruits(ar, 40, 50, i, j, type="column")
                diagonal = get_fruits(ar, 40, 50, i, j, type="diagonal")
                anti_diagonal = get_fruits(ar, 40, 50, i, j, type="anti-diagonal")

                ls = [row, column, diagonal, anti_diagonal]


                if max(ls) > mostEli:
                    # 当前切割下的切割方式
                    way = ls.index(max(ls))
                    mostEli = max(ls)
                    max_x = i
                    max_y = j

            cut_fruit(ar, 40, 50, max_x, max_y, way)
            remain -= mostEli
            cut_num += 1

    
    return cut_num

if __name__ == "__main__":
    print(main())