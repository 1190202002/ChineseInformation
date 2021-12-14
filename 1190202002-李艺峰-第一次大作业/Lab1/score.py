all_word=0
right_word=0
with open("Lab1\标椎结果.txt",'r',encoding='utf-8') as yes:
    rights=yes.readlines()
    good=set()
    pre=set()
with open("Lab1\前配分词结果.txt",'r',encoding='utf-8') as pre:
        ps=pre.readlines()
        for (right,p) in zip(rights,ps):
            good=set(right.split("\\"))
            pre=set(p.split("\\"))
            g=good&pre
            right_word+=len(g)
            all_word+=len(good)
score=right_word/all_word*100
print("正向匹配正确率："+str(score)+"%")
all_word=0
right_word=0

with open("Lab1\后配分词结果.txt",'r',encoding='utf-8') as pre:
        ps=pre.readlines()
        for (right,p) in zip(rights,ps):
            good=set(right.split("\\"))
            pre=set(p.split("\\"))
            g=good&pre
            right_word+=len(g)
            all_word+=len(good)
score=right_word/all_word*100
print("逆向匹配正确率："+str(score)+"%")

with open("Lab1\双配分词结果.txt",'r',encoding='utf-8') as pre:
        ps=pre.readlines()
        for (right,p) in zip(rights,ps):
            good=set(right.split("\\"))
            pre=set(p.split("\\"))
            g=good&pre
            right_word+=len(g)
            all_word+=len(good)
score=right_word/all_word*100
print("双向匹配正确率："+str(score)+"%")

