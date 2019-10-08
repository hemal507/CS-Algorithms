def evenNumbersBeforeFixed(s, f):
    r=0
    for i in s :
        if i == f :
            return r
        r += i % 2 == 0 
    return -1

from itertools import takewhile
def evenNumbersBeforeFixed2(s,f) :
	r=len(filter(lambda x: x%2==0 , (takewhile(lambda x : x!=f , s))))
	return -1 if r==0 else r

