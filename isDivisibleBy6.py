import re
def isDivisibleBy6(s):
	return [re.sub('\*',str(x),s) for x in range(10) if int(re.sub('\*',str(x),s)) % 6 == 0]

def isDivisibleBy6(s):
	return [str(y) for y in [ int(re.sub('\*',str(x),s)) for x in range(10) ] if y % 6 ==0    ]
	
print(isDivisibleBy6('1*0'))
