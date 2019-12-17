import re
sumUpDigits = lambda s : sum(int(x) for x in re.findall('\d',s))
