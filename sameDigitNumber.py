def sameDigitNumber(n):
    i = str(n)[0]
    if i * len(str(n)) == str(n) :
        return True
    return False
