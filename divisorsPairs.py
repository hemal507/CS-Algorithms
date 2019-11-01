from itertools import combinations
def divisorsPairs(sequence):
    return sum( [x[0] < x[1]  for x in list(combinations(sequence,2)) ]) 

