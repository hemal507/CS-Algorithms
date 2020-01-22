def excelSheetColumnNumber(s):
    v, j = 0, 0
    for i in s[::-1]:
        v += pow(26, j) * (ord(i) - 64)
        j += 1
    return v


print(excelSheetColumnNumber('AB'))
