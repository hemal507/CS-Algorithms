def variableName(name):
    if name[0].isdigit() :
        return False
    if len([x for x in name if (x.isalpha()) or (x.isdigit()) or x == '_' ]) == len(name) :
	return True 
    else :
	return False    

