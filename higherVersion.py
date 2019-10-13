def higherVersion(v1, v2):
        l1 = v1.split(".")
        l2 = v2.split(".")
        for i in range(len(l1)) :
                if int(l1[i]) < int(l2[i]) :
                        return False
                elif int(l1[i]) > int(l2[i]) :
                        return True
        return False

def higherVersion(v1, v2):
        return map(int, v1.split('.')) > map(int, v2.split('.'))
