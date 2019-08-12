def firstDuplicate(a):
	dups = {}
	
	for i in a :
		if i in dups :
			dups[i] += 1
		else :
			dups[i] = 1
		if dups[i] == 2 :
			print(dups)
			return i

	print(dups)
	return -1


def firstDuplicate2(a):
	set_a = set()
        for i in a :
                if i in set_a :
                        return i
                else :
                        set_a.add(i)
        return -1

print(firstDuplicate2([2, 1, 3, 5, 3, 2]))
