countVowelConsonant = lambda s : sum([1 if x in 'aeiou' else 2 for x in s ])

print(countVowelConsonant('acde'))