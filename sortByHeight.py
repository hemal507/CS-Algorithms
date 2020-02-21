def sortByHeight(a) :
    s=sorted([x for x in a if x != -1 ])
    r=[]
    j=0
    for i in a :
        if i == -1 :
            r.append(i)
        else :
            r.append(s[j])
            j +=1
    return r

print(sortByHeight( [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]))