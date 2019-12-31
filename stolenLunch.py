def stolenLunch(note):
    r=[]
    for i in note:
        if i.isdigit() :
            r.append(chr(ord(i)+49))
        elif ord(i) <= 106 and ord(i) >=97 :
            r.append(str( ord(i) - ord('a') )  )
        else :
            r.append(i)
    return ''.join(r)
        
        
print(stolenLunch("you'll n4v4r 6u4ss 8t: cdja") )
