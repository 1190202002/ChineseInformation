from os import close
outpath="Lab1\处理后词表.txt"          #处理后生成的词表
infile="Lab1\处理后语料.txt"              #要处理的语句
resultfile="Lab1\分词结果.txt"       #分词结果
max_word_length=6                         #词典中最长词的长度，自动计算
#根据词表生成分词词典word_dict，词存储在word_dict集合中
def creat_word_dict(outpath):
    word_dict=set()
    with open(outpath,'r',encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
           if len(line)<=max_word_length:
              word_dict.add(line.split("\n")[0])
    f.close
    return word_dict
