import re
def increaseNumberRoundness(n) :
	l=[x for x,y in enumerate(`n`) if y == '0']
	if len(l) == 0 or (len(l) > 1 and l[0] == l[1]-1) :
		return False
	return True
		
