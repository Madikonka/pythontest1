import re
def arrowy(astr):
    #x = astr.replace('<'[-]+'>', "111111")
    x = re.sub(r'<[-]+>', '', astr).replace(" ", "")
    y = re.sub(r'<[=]+>', '', x)
#new commit for main
    ss=0
    oup=[]
    for i in y:
       # if i=="1":
         #   oup.append(i)  
        if i=="-":
            ss+=1
        else:
            if ss!=0: oup.append(ss)            
            if (i=="<"): oup.append(-1)
            if (i==">"): oup.append(1)
            ss=0    
    print(oup)
   # print("------------------")
    #for i in oup[::-2]:
    #    print (i)

arrowy("<------- ... > >>---->")

