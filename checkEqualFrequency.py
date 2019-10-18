def checkEqualFrequency(inputArray):
    return True if len(set([inputArray.count(i) for i in set(inputArray)])) == 1 else False


