#using lambda
def arrayReplace(p, q, r):
    return map(lambda x : r if x == q else x, p)

#using list comprehension
def arrayReplace(p, q, r):
    return [r if i == q else i for i in p]

