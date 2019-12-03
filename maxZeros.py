def maxZeros(n):
        p=[0]*n
        for i in range(2,n+1) :
                r=[]
                z=n
                while z > 0 :
                        p[i-1] += z%i==0
                        z /= i
        return p.index(max(p))+1

