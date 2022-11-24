import re
def isLeapYear(year):
    res = lambda i: (re.findall(r'\d+', i))
    inList = (res(year))
    year1 = year.split(" ")

    resu = sorted(list(zip(inList,year1)))
   # resu1 = " ".join(x[1] for x in resu)
   # print(resu1)

    resu1 = (' '.join(sorted(year.split(), key=lambda ddddd:sorted(ddddd))))
    #print (list(lambda w:sorted(w)))
    ah = (lambda ddddd:sorted(ddddd))
    print(ah("is2 Thi1s T4est 3a mayb6e something5"))
isLeapYear("is2 Thi1s T4est 3a mayb6e something5")