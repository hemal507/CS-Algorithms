"""
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


def firstNotRepeatingCharacter(s):
    return ([x for x in s if s.index(x) == s.rindex(x)] + ['_'])[0]
"""


def firstNotRepeatingCharacter(s):
    for x in s:
        if s.find(x) == s.rfind(x):
            return x
    return '_'
