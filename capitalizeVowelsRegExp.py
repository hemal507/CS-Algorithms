def capitalizeVowelsRegExp(input):
	return ''.join([x.upper() if x in 'aeiouy' else x for x in input ])

import re
capitalizeVowelsRegExp = lambda s : re.sub('[aeiouy]',lambda x : x.group(0).upper(),s)
