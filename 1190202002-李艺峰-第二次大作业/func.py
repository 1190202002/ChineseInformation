from collections import OrderedDict
def cretrain(filePath):
    f = open(filePath, 'r', encoding='utf-8', errors='ignore')
    wordlists, taglists = [], []
    wordlist, taglist = [], []
    for line in f.readlines():
        if line == '\n':
            wordlists.append(wordlist); taglists.append(taglist)
            wordlist, taglist = [], []
        else: 
            word, tag = line.strip('\n').split()
            wordlist.append(word); taglist.append(tag)
    if len(wordlist) != 0 or len(taglist) != 0:
        wordlists.append(wordlist); taglists.append(taglist)
    f.close()
    return wordlists, taglists
#字符串根据字典转数字
def str2int(origin, dictionary):
    result = []
    if isinstance(origin[0], list):
        for i in range(len(origin)):
            result.append([])
            for j in range(len(origin[i])):
                if origin[i][j] in dictionary:
                  result[i].append(dictionary[origin[i][j]])
                else:
                    result[i].append(-1)
    else:
        for i in range(len(origin)):
            result.append(dictionary[origin[i]])
    return result

#生成字典
def creDict(fileNameList):
    wordDict = OrderedDict()
    for fileName in fileNameList:
        f = open(fileName, 'r', encoding='utf-8', errors='ignore')
        for line in f.readlines():
            if line == '\n': continue
            word, tag = line.strip('\n').split()

            if word not in wordDict:
                wordDict[word] = len(wordDict)
        f.close()
    return wordDict

#计算准确率和召回率
def accuracy(name):
   rtWordLists, rtTagLists = cretrain('data\\right_test.txt')
   rname=set()

   for i in range(len(rtTagLists)):
      for j in range(len(rtTagLists[i])):
        if(rtTagLists[i][j-1]=="B-NAME" and rtTagLists[i][j]=="M-NAME" and rtTagLists[i][j+1]=="E-NAME"):
            rname.add(rtWordLists[i][j-1]+rtWordLists[i][j]+rtWordLists[i][j+1])
        elif(rtTagLists[i][j-1]=="B-NAME" and rtTagLists[i][j]=="E-NAME"):
            rname.add(rtWordLists[i][j-1]+rtWordLists[i][j])
   with open("data/rightname.txt",'w',encoding='utf-8') as f:
    for n in rname:
        f.writelines(n+"\n")
   pre=str(len(name&rname)/len(name))
   print("准确率："+pre)
   rcall=str(len(name&rname)/len(rname))
   print("召回率："+rcall)
#识别出名字
def recname(tagPall,testWordLists):
    name=set()
    for i in range(len(tagPall)):
       for j in range(len(tagPall[i])):
          if(tagPall[i][j-1]==0 and tagPall[i][j]==1 and tagPall[i][j+1]==2):
            name.add(testWordLists[i][j-1]+testWordLists[i][j]+testWordLists[i][j+1])
          elif(tagPall[i][j-1]==0 and tagPall[i][j]==2):
            name.add(testWordLists[i][j-1]+testWordLists[i][j]) 
    return name