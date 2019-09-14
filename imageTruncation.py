def imageTruncation(image, threshold):
    return [ [x if x <= threshold else threshold for x in a  ] for a in image ]

