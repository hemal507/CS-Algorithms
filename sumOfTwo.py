def sumOfTwo(a, b, v):
    sa=set(a)
    sb=set(b)
    for i in sa :
        if v-i in sb :
            return True
    return False


