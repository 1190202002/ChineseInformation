import re
inpath="Lab1\词表.txt"            #未经处理的词表
outpath="Lab1\处理后词表.txt"          #处理后生成的词表
def creat_dict(inpath,outpath):
    word_dict=set()
    with open(inpath,'r',encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
           word=re.split(' |\n|\t',line)[0]
           if len(word)<=6 :
              word_dict.add(word)
    
    f.close
    with open(outpath,'w',encoding='utf-8',) as w:
        for word in word_dict:
           w.write(str(word)+"\n")
    w.close
    return word_dict

creat_dict(inpath,outpath)