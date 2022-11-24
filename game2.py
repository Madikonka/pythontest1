import re
def arrowy(astr):
    #x = astr.replace('<'[-]+'>', "111111")
    x = re.sub(r'<[-]+>', '', astr).replace(" ", "")
    y = re.sub(r'<[=]+>', '', x)
   # print(x)
    print(y)
    s=0
    for i in y:
        if i==">":
            s+=1
        elif 


arrowy("       1   sdjknv     <--->")

