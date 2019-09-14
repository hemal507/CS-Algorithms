def imageTruncation(image, threshold):
    return [ [x if x <= threshold else threshold for x in a  ] for a in image ]

# alternative solution
def imageTruncation(i, j):
    return [ [[x,j][x>j] for x in a  ] for a in i ]

