def surpasserCount(a):
    return sum([y > a[x] for x in range(len(a)) for y in a[x + 1:]]) % 1000000007


print(surpasserCount([1, 2, 3, 4, 5]))
