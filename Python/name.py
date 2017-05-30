from __future__ import unicode_literals
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime


# 从网页中提取名字，并清洗数据，存入name.txt
def GetFirstName(url):
    # 爬取页面，使用BeautifulSoup处理
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    fp = open("name.txt", "w", encoding='utf-8')
    # 查找内容
    for words in soup.find("div", {"class": "BNE_main"}).findAll("p"):
        # 提取文本
        uni = words.get_text()
        # 使用正则匹配匹配名字，如果是两个中文字的话，匹配成功
        match = re.search(r"^(　　)[\u4e00-\u9fa5][\u4e00-\u9fa5]( ).+$", uni)
        if match:
            # 如果匹配成功，写入文件
            fp.writelines(match.group(0) +"\n")
        else:
            # 如果匹配失败，再次匹配，看是否为格式化的单个中文字的内容
            match = re.search(r"([\u4e00-\u9fa5]、)", uni)
            if match:
                # 如果匹配成功，写入文件
                fp.writelines(match.group(0) + "\n")
    fp.close()

    # 在匹配后，内容还是有些“脏”，这时候需要清洗数据

    # 打开两个文件，一个是脏数据，一个是清洗后的数据
    fp = open("name.txt", "r", encoding='utf-8')
    out = open("name_washed.txt", "w", encoding='utf-8')
    # 分别替换tab，标点，并把空格替换为换行，方便下一步的加入list
    for line in fp:
        line_washed = line.replace("　　", "")
        line_washed = line_washed.replace("、", "")
        line_washed = line_washed.replace(" ", "\n")
        out.write(line_washed)
    fp.close()
    out.close()

# 从wiki的百家姓页面爬取百家姓内容
def LastNameFromWiki(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    fp = open("LastName.txt", "w", encoding='utf-8')
    names = soup.find("div", {"class": "poem"}).find("div", {"class": "poem"}).get_text()
    names_washed = names.replace("　", "")
    names_washed = names_washed.replace("\n", "")
    fp.write(names_washed)
    fp.close()

First_name_url = "http://blog.sina.com.cn/s/blog_4a1e8c130102vgss.html"
wikiurl = "https://zh.wikisource.org/zh-hans/%E7%99%BE%E5%AE%B6%E5%A7%93"

# GetFirstName(First_name_url)
# LastNameFromWiki(wikiurl)

first_name = []
last_name = []
random.seed(datetime.datetime.now())

# 把姓氏添加到list中
fp = open("LastName.txt", "r", encoding='utf-8')
i = fp.read(1)
while(i != ""):
    last_name.append(i)
    i = fp.read(1)
fp.close()

# 把名字添加到list中
fp = open("name_washed.txt", "r", encoding='utf-8')
for i in fp.readlines():
    first_name.append(i.strip())

# 随机产生5个名字
for i in range(5):
    first = first_name[random.randint(0, len(first_name)-1)]
    last = last_name[random.randint(0, len(last_name)-1)]
    print(last + first)