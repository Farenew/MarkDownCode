import jieba
import jieba.posseg as ps

fp = open("doupo.txt", "r")
fsort = open("words_list.txt", "w")
# 按照行来统计
for line in fp.readlines():
    clean_line = line.strip()
    # 每行都做一个jieba的分词，这里用默认模式，也就是精准分词
    word_list = ps.cut(clean_line)
    # 对于分的词，如果不在STOPWORDS里，就写入文件
    for word in word_list:
        # 这里写入的方式是在词与词性间添加了一个空格，便于后续读取
        fsort.writelines(str(word.word) + ' ' + str(word.flag) + '\n')
fp.close()
fsort.close()

print("jieba cut is finished\n")