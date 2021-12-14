from os import close
import re
path="Lab1\语料.txt"
outpath="Lab1\处理后语料.txt"
def yuliao():
   with open(outpath,'w',encoding='utf-8') as w:
       with open(path,'r',encoding='utf-8') as r:
            lines=r.readlines()
            for line in lines:
              sens=re.split('。|！|？',line)
              for sen in sens:
                  if(len(sen)>1):
                   w.write(sen)
                   w.write("\n")
       r.close
   w.close
    
    
yuliao()