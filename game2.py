import re
def arrowy(astr):
    #x = astr.replace('<'[-]+'>', "111111")
    x = re.sub(r'<[-]+>', '', astr).replace(" ", "")
    y = re.sub(r'<[=]+>', '', x)
   # print(x)
    #print(y)
    ss=0
    oup=""
    for i in y:
        if i=="-":
            ss+=1
            #oup+=oup
        else:
            oup=str(ss)+i
            ss=0    


    """count '-' in '-->' pattern """
    print(oup)


arrowy("-------> !! --->")

