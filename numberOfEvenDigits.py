def numberOfEvenDigits(n) :
    return len(filter(lambda x : int(x)%2==0, str(n)))

def numberOfEvenDigits1(n) :
    return len([x for x in str(n) if int(x) % 2 == 0])
