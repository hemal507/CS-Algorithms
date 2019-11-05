def capitalizeVowelsRegExp(input):
	return ''.join([x.upper() if x in 'aeiouy' else x for x in input ])

