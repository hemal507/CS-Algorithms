def isPowerOfTwo2(n):
    return all(i == '0' for i in bin(n)[3:])


print(isPowerOfTwo2(116))
