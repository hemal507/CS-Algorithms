import re
sumUpDigits = lambda s : sum(int(x) for x in re.findall('\d',s))

sumUpDigits = lambda s : sum(map(int, re.findall('\d',s)))                             
