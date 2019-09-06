from collections import OrderedDict
def firstNotRepeatingCharacter(s):
    d=OrderedDict()
    l=''
    for i in s :
        d[i] = d.get(i,0) + 1
    for k,v in d.items() :    
        if v == 1 :
            return k
    return '_'    


