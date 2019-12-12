class Prizes(object):
    def __init__(self, purchases, n, d):
        self.i = 1
        self.purchases = purchases
        self.n = n
        self.d = d

    def __iter__(self):
        return self

    def next(self):
        if self.i < len(self.purchases) + 1:
            i = self.i
            self.i += 1
            if i % self.n == 0 and self.purchases[i-1] % self.d == 0:
                return i
            else:
                return self.next()        
        else:
            raise StopIteration

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

print(superPrize( [64, 67, 86, 87, 69, 49, 47, 75, 43, 74, 23, 47, 77, 83, 67, 24, 11, 59, 19, 88] ,4,5)) 
