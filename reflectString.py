def reflectString(i):
    return ''.join([chr(219 - ord(x)) for x in i])
#    return ''.join(map(lambda x : chr(219 - ord(x) ), i))
