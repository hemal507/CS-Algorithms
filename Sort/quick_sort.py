import numpy as np

# generate a random array
#X = np.random.randint(1000,size=10)
##X=[242, 903 , 751 ,219 ,775 ,102, 314 ,687 ,320 ,300 ,859]
X = [7,8,1,5,4,9,2]
##X = [2,1,4,5,7,8,9]
print('UNSORT: ', X)

## quick sort
## select a pivot - median of first last and mid of the list
## < pivot are placed towards the left of pivot
## > pivot are placed towards the right of the pivot
## recursively repeat this
## divide and conquer problem

def get_pivot(X):
    mid = X[len(X)//2]
    first = X[0]
    last = X[len(X)-1]
    if first < mid:
        pivot = mid
    else:
        pivot = first
        
    if pivot > last:
        pivot = last


def quick_sort(X):
    pivot = get_pivot(X)
    
    
