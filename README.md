# MarkDownCode
Some useful pieces of code.

## Python 部分(Python Part)

---

### 1. 随机名字产生器(Random Chinese name generator)

[name.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/name.py)


通过爬取附有常用名字的一个博客，以及wiki的百家姓，建立一个姓与名的list，然后通过随机数随机选取内容，产生名字

---

By crawling names from blog and wikipedia, we obtain lists about first name and last name. Using random numbers to choose from lists built, we can generate some typical Chinese names.

### 2. 格式化随机数(format randint())

[random_format.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/random_format.py)


一个极其简单的demo演示如何格式化随机数字

---

A very simple demo about how to format random numbers from random.randint() method

### 3. 微信自动回复(wechat auto respond)

[wechat_respond.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/wechat_respond.py)


通过itchat连接微信小冰来做微信的自动回复

2019-3-28更新:

    重新上传了代码, 可以通过回复88xiaoice来自动关闭小冰.

---

A very simple demo about how to format random numbers from random.randint() method

### 4. 帮别人做的几道华为面试题(some code wrote for others)

题在代码里介绍

- 切水果问题

    [cut_fruit.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/cut_fruit.py)

- 最短路径

    [minimum_path.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/minimum_path.py)

- 大端小端

    [bigEndian_littleEndian.py](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/bigEndian_littleEndian.py)

### 5. 一个简单的分词练习

很早的时候写的代码了, 风格很烂....直接放到这里了.

[链接](https://github.com/ForenewHan/MarkDownCode/blob/master/Python/doupo/)

- 首先在doupo\_fenci里面，实现了使用jieba对小说的分词。
  - 运行jieba\_doupo.py可以对全文分词.
  - 运行jieba\_cixing.py可以对小说分词同时写入.
  - 词性分词后会产生一个words\_list.txt的文件
  - 这个文件是后面两个分析的基础文件，应该把这个文件拷贝到另外两个文件夹里。
- 然后在doupo_analysis里有初步的分析。
  - 第一个分析是对所有的词做一个词频的分析
  - 第二个分析是对具体的类别做的分析.
  - 他们运行的基础都是words_list.txt这个文件
- 最后是一个词性分析的demo，在doupo\_cixing里，按照形容词做了一个分析，这里要求分词文件word\_list.txt是运行了jieba\_fenci里的jieba\_cixing.py的结果

## 其他(others)

### 1. 关于Atom下markdown-themeable-pdf格式的文件

[markdown-themeable-pdf](./Others/readme.md)


自定义的markdown-themeable-pdf输出格式

---

Some files about how to customize your output format by markdown-themeable-pdf in Atom.
