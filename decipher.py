def decipher(s) :
        r=[]
        while len(s) > 0 :
                if s[0] == '1' :
                        r.append(chr(int(s[:3])))
                        s = s[3:]
                else :
                        r.append(chr(int(s[:2])))
                        s =s[2:]
        return ''.join(r)
