def arrayPacking(a) :
    return int(''.join([bin(i)[2:].rjust(8,'0')]))
    