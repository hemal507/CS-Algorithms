def leastFactorial(n):
    fact=1
    for i in range(1,n+1) :
        fact *= i
        if fact >= n :
            return fact
        

