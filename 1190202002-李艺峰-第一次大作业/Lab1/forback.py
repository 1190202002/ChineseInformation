from os import close
import worddict
import forwardmatch
import backmatch
outpath="Lab1\处理后词表.txt"          #处理后生成的词表
infile="Lab1\处理后语料.txt"              #要处理的语句
resultfile="Lab1\双配分词结果.txt"       #分词结果
max_word_length=6                         #词典中最长词的长度，自动计算
punish_singleword=1                  #单字词惩罚因数
punish_notindict=1                   #非字典词惩罚因数
punish_allword=1                     #总词数惩罚因数

#双向匹配,比较单字词、非字典词、总词数数量的数量
def forback_match(f_result,b_result):
    fb_result=[]
    for i in range(0,len(f_result)):
        fsingleword=0
        fnotdic=0
        bsingleword=0
        bnotdic=0
        f_punish=0
        b_punish=0
        fallword=len(f_result[i])
        ballword=len(b_result[i])
        for word in f_result[i]:
          if len(word)==1:
              fsingleword+=1
          if word not in word_dict:
              fnotdic+=1
        for word in b_result[i]:
          if len(word)==1:
              bsingleword+=1
          if word not in word_dict:
              bnotdic+=1
        f_punish=fsingleword*punish_singleword+fnotdic*punish_notindict+fallword*punish_allword
        b_punish=bsingleword*punish_singleword+bnotdic*punish_notindict+ballword*punish_allword
        if(f_result[i]==b_result[i]):
           fb_result.append(f_result[i])
        else:
            if(f_punish<=b_punish):
                fb_result.append(f_result[i])
            else:
                fb_result.append(b_result[i])
    return  fb_result

def storeresult(fb_result,resultfile):
    with open(resultfile,'w',encoding='utf-8') as res:
    #双向匹配最终二者之间选择的分词结果
        
        for line in fb_result:
           for word in line:
               res.write(str(word)+"\\")
        res.write("\n")

    res.close

if __name__=='__main__':
    word_dict=[]
    word_dict=worddict.creat_word_dict(outpath)
    f_result=forwardmatch.forward_max_match(infile,word_dict,max_word_length)
    b_result=backmatch.back_max_match(infile,word_dict,max_word_length)
    fb_result=forback_match(f_result,b_result)
    storeresult(fb_result,resultfile)