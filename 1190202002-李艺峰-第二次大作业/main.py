from os import name
from func import *
from HMM import *

#获得字典，每个字对应唯一数字
wordDict = creDict(['data\\train.txt'])

#定义标签字典
tagDict = {'B-NAME': 0, 'M-NAME': 1, 'E-NAME': 2, 'O': 3, 'B-CONT': 4, 'M-CONT': 5, 'E-CONT': 6, 'B-EDU': 7,  
    'M-EDU': 8, 'E-EDU': 9, 'B-TITLE': 10, 'M-TITLE': 11, 'E-TITLE': 12, 'B-ORG': 13, 'M-ORG': 14, 'E-ORG': 15, 
        'B-RACE': 16, 'E-RACE': 17, 'B-PRO': 18, 'M-PRO': 19, 'E-PRO': 20, 'B-LOC': 21, 'M-LOC': 22, 'E-LOC': 23,
         'S-RACE': 24, 'S-NAME': 25, 'M-RACE': 26, 'S-ORG': 27, 'S-CONT':28, 'S-EDU':29,'S-TITLE':30, 'S-PRO':31,
         'S-LOC':32}

#训练集数据
trainWordLists, trainTagLists = cretrain('data\\train.txt')


#测试集数据
testWordLists=[]
with open("data/test.txt",'r',encoding='utf-8') as t:
    lines=t.readlines()
    for line in lines:
        testWordLists.append(list(line))
#HMM方法
hmm = HMM(len(wordDict), len(tagDict))
hmm.trainhmm(str2int(trainWordLists,wordDict), str2int(trainTagLists,tagDict))
tagPall=hmm.test(str2int(testWordLists, wordDict))

            
name=recname(tagPall,testWordLists)
with open("data/name.txt",'w',encoding='utf-8') as fna:
    for n in name:
        fna.writelines(n+"\n")
print("识别名字：\n")
for i in name:
    print(i)

accuracy(name)




