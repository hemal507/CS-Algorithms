def digitDistanceNumber(n):
    return int(''.join([str(abs(int(x) - int(y))) for x,y in zip(`n`[1:],`n`[:-1])]))    

def digitDistanceNumber(n):
    i=map(int,`n`)
    return reduce(lambda x,y : x*10+y,[abs(i[j+1]-i[j]) for j in range(len(i)-1)   ])
