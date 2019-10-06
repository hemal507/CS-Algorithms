import itertools
def countIncreasingSequences(n, k):
    return len(list(itertools.combinations(range(1,k+1),n)))        
        
