import math
def caesarBoxCipherEncoding(a):
    l=int(math.sqrt(len(a)))
    q=[ [a[i+j:i+j+1] for i in range(0, len(a), l)]  for j in range(l) ]
    print(q)
    return ''.join([''.join(i) for i in q])

print(caesarBoxCipherEncoding('sixteenletters16'))
