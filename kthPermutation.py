from itertools import permutations

def kthPermutation(numbers, k):
    return list(list(permutations(numbers,len(numbers)))[k-1])

print(kthPermutation ([1, 2, 3, 4, 5] ,4 ) )
