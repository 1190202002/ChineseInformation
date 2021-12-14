from os import close
import worddict
outpath="Lab1\处理后词表.txt"          #处理后生成的词表
infile="Lab1\处理后语料.txt"              #要处理的语句
resultfile="Lab1\前配分词结果.txt"       #分词结果
max_word_length=6                         #词典中最长词的长度，自动计算
#正向最大匹配
def forward_max_match(infile,word_dict,max_word_length):
    with open(infile,'r',encoding='utf-8') as file:
        lines=file.readlines()
        f_result=[]
        for line in lines:
            f_word_res=[]
            start=0
            while start<len(line):
                for step in range(max_word_length,1,-1):
                    match=False
                    if line[start:start+step] in word_dict:
                        f_word_res.append(line[start:start+step])
                        start+=step
                        match=True
                        break
                if not match:
                    f_word_res.append(line[start])
                    start+=1 
            f_result.append(f_word_res)
    file.close
    return f_result


def storeresult(f_result,resultfile):
    with open(resultfile,'w',encoding='utf-8') as res:
    #正向匹配分词结果
        
        for line in f_result:
           for word in line:
               res.write(str(word)+"\\")
        res.write("\n")
    res.close

if __name__=='__main__':
    word_dict=[]
    word_dict=worddict.creat_word_dict(outpath)
    f_result=forward_max_match(infile,word_dict,max_word_length)
    storeresult(f_result,resultfile)
    