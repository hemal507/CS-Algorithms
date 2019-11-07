import re
def replaceAllDigitsRegEx(inputString):
	return re.sub('\d','#',inputString)
