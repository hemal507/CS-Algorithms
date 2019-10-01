def correctLineup(athletes):
    return [athletes[i+1 if i%2 ==0 else i-1 ] for i in range(len(athletes))]

