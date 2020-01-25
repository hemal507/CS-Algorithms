"""
def isPowerOfTwo2(n):
    return all(i == '0' for i in bin(n)[3:])
"""


def isPowerOfTwo2(n):
    return n & (n - 1) < 1


print(isPowerOfTwo2(116))
