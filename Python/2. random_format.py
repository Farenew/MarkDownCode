from __future__ import unicode_literals
import random
import datetime

random.seed(datetime.datetime.now())

# 格式化的随机数的一个demo，产生5个随机数
for i in range(10):
    # 40到45之间的随机数
    rand1 = random.randint(40, 45).__format__('02')
    # 0到16之间，表示00年到16年之间，但用两位数显示
    rand2 = random.randint(0, 16).__format__('02')
    # 1到12之间，表示1月到12月
    rand3 = random.randint(1, 12).__format__('02')
    # 1到30，表示1号到30号
    rand4 = random.randint(1, 30).__format__('02')
    # 1到5
    rand5 = random.randint(1, 5).__format__('02')
    
    print(rand1 + rand2 + rand3 + rand4 + rand5)