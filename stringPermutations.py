from itertools import permutations as p

stringPermutations = lambda s: sorted([''.join(i) for i in set(p(s, len(s)))])
