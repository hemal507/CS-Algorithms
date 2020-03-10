def kthLargestElement(n, k) :
    return sorted(n, reverse=True)[k-1]

print(kthLargestElement([-1, 2, 0],3))