def minimumOnStack(s) :
    r=[]
    t=[]
    for i in s :
        if 'min' in i :
            r.append(min(t))
        elif 'pop' in i :
            t.pop()
        else :
            t.append(int(i.split()[1]))
    return r

print(minimumOnStack(["push 10",
 "min",
 "push 5",
 "min",
 "push 8",
 "min",
 "pop",
 "min",
 "pop",
 "min"]))