"""

def excelSheetColumnNumber(s):
    v, j = 0, 0
    for i in s[::-1]:
        v += pow(26, j) * (ord(i) - 64)
        j += 1
    return v

"""

from functools import reduce


def excelSheetColumnNumber(s):
    return reduce(lambda x, y: x * 26 + ord(y) - 64, s, 0)


print(excelSheetColumnNumber('AB'))
