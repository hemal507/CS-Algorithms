def columnTitle(n):
    t = ''
    while n:
        n-=1
        t+=chr(n % 26 + 65)
        n//=26
    return t[::-1]


print(columnTitle(16808))