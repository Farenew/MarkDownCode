import re

words_dict = {}
fp = open("words_list.txt", "r")
for k in fp.readlines():
    i = k.strip()
    # 匹配空格以前的内容
    word = re.match(".+( )", i)
    # 把空格及空格以前的内容删除，留下后面的词性标识
    flag = re.sub(".+( )", "", i)
    if flag == "a":
        if word.group(0) in words_dict:
            words_dict[word.group(0)] += 1
        else:
            words_dict[word.group(0)] = 1
fp.close()

print("the dict is finished\n")

sort_list = []
for key, value in words_dict.items():
    if value > 20 and len(key) > 2:
        sort_list.append((value, key))
sort_list.sort(reverse=True)
fp = open("sort_by_xingrongci.txt", "w")
for value, key in sort_list:
    fp.writelines(str(key)+"---"+str(value)+"\n")
fp.close()


