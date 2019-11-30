def makeArrayConsecutive(sequence):
    return [x for x in range(min(sequence)+1, max(sequence)) if x not in sequence]
    
makeArrayConsecutive = lambda sequence : [x for x in range(min(sequence)+1, max(sequence)) if x not in sequence]
