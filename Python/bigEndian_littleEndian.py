# -*- coding: utf-8 -*-
"""

# 题

非常简单的一个题....判断字符串正序还是逆序输出, 但是题里面包装了一下, 说到了大端和小端, 就很迷惑.

# 输入

输入一个数字, 表示后续几个字符串的输入. 每个字符串以0或者1开始, 说明了要正序还是逆序输出. 全部内容输入之后, 做输出.



"""

x = input()
x = int(x)

stringList = list()

for i in range(x):
    string = input()
    tag = string[0]
    string = string[1:len(string)]

    if tag == '0':
        string = string[::-1]
        stringList.append(string)
    elif tag == '1':
        stringList.append(string)


for i in reversed(stringList):
    print(i, end=' ')



