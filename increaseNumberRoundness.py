def increaseNumberRoundness(n) :
        l=[x for x,y in enumerate(`n`) if y == '0']
        if len(l) == 0 or (len(l) > 1 and l[0] == l[1]-1) or (len(l) == 1 and `n`.index('0') == len(`n`)-1) :
                return False
        return True

import re
def increaseNumberRoundness(n) :
        return bool(re.search('0[1-9]',`n`))
