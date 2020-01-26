import re


def classifyStrings(s):
    if '?' not in s:
        return 'bad' if re.search(r'([bcdfghjklmnpqrstvwxyz]{5}|[aeiou]{3})', s) else 'good'
    p = s.index('?')
    sv = classifyStrings(s[:p] + 'a' + s[p + 1:])
    sc = classifyStrings(s[:p] + 'b' + s[p + 1:])
    return 'mixed' if sv != sc else sv

print(classifyStrings('aeu'))
