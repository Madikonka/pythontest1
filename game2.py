import re
def arrowy(astr):
    #x = astr.replace('<'[-]+'>', "111111")
    x = re.sub(r'<[-]+>', '', astr).replace(" ", "")
    y = re.sub(r'<[=]+>', '', x)
   # print(x)
    #print(y)
    ss=0
    oup=""
    """count '-' in '-->' pattern """
    for i in y:
        if i=="-":
            ss+=1
        else:
            oup=str(ss)+i
            ss=0    


    
    print(oup)


arrowy("-------> !! --->")

