def digitDistanceNumber(n):
    return int(''.join([str(abs(int(x) - int(y))) for x,y in zip(`n`[1:],`n`[:-1])]))    


