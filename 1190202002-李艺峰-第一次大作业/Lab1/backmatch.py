from os import close
import worddict
outpath="Lab1\处理后词表.txt"          #处理后生成的词表
infile="Lab1\处理后语料.txt"              #要处理的语句
resultfile="Lab1\后配分词结果.txt"       #分词结果
max_word_length=6                         #词典中最长词的长度，自动计算
#逆向最大匹配
def back_max_match(infile,word_dict,max_word_length):
    with open(infile,'r',encoding='utf-8') as file:
        lines=file.readlines()
        b_result=[]
        for line in lines:
            b_word_res=[]
            start=len(line)
            while start>0:
                for step in range(min(max_word_length,start),0,-1):
                    match=False
                    if line[start-step:start] in word_dict:
                        b_word_res.append(line[start-step:start])
                        start-=step
                        match=True
                        break
                if not match:
                    start-=1
                    b_word_res.append(line[start])
            b_word_res.reverse()
            b_result.append(b_word_res)
    file.close
    return b_result
def storeresult(b_result,resultfile):
    with open(resultfile,'w',encoding='utf-8') as res:
    #逆向匹配分词结果
        
        for line in b_result:
           for word in line:
               res.write(str(word)+"\\")
        res.write("\n")
if __name__=='__main__':
    word_dict=[]
    word_dict=worddict.creat_word_dict(outpath)
    b_result=back_max_match(infile,word_dict,max_word_length)
    storeresult(b_result,resultfile)