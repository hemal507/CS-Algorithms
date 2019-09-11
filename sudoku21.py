def sudoku2(grid):
    for i in grid :
        for j in i :
            if j != "." and i.count(j) > 1 :
                return False
	
    for x in zip(*grid) :
        for y in x :
            if y != "." and x.count(y) > 1 :
                return False

    r=range(3)
    y=[]
    t=[]
    for m in r :
	for n in r :
		t.append( a[m][n] )
    y.append(t)
    t=[]
    for m in r  :
	for n in [x+3 for x in r] :
		t.append(a[m][n])
    y.append(t)
    t=[]	
    for m in r :
	for n in [x+6 for x in r]:
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+3 for x in r]:
	for n in r :
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+3 for x in r] :
	for n in [u+3 for u in r] :
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+3 for x in r] :
	for n in [u+6 for u in r] :
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+6 for x in r] :
	for n in r :
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+6 for x in r] :
	for n in [u+3 for u in r] :
		t.append(a[m][n])
    y.append(t)
    t=[]
    for m in [x+6 for x in r] :
	for n in [u+6 for u in r] :
		t.append(a[m][n])
    y.append(t)
    print(y)
    for i in y :
        for j in i :
            if j != "." and i.count(j) > 1 :
                return False

    return True        

a=[[".","4",".",".",".",".",".",".","."], 
 [".",".","4",".",".",".",".",".","."], 
 [".",".",".","1",".",".","7",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".","3",".",".",".","6","."], 
 [".",".",".",".",".","6",".","9","."], 
 [".",".",".",".","1",".",".",".","."], 
 [".",".",".",".",".",".","2",".","."], 
 [".",".",".","8",".",".",".",".","."]]

print(sudoku2(a))
