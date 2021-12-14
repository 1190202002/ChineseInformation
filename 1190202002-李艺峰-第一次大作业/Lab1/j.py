import jieba
with open("Lab1\处理后语料.txt",'r',encoding='utf-8') as f:
    ls=f.readlines()
    with open("Lab1\标椎结果.txt",'w',encoding='utf-8') as p:
       for l in ls:
         w=jieba.cut(l)
         p.write("\\".join(w))

