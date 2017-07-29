import numpy as np

# generate a random array
#X = np.random.randint(1000,size=10)
##X=[242, 903 , 751 ,219 ,775 ,102, 314 ,687 ,320 ,300 ,859]
X = [7,8,1,5,4,9,2]
##X = [2,1,4,5,7,8,9]
print('UNSORT: ', X)

## merge sort
## halfs the list recursively until there is one element in it
## then starts to sort from the single element list to up ward recursively
## to build the oroginal list

## since it has to call recursively the merge step - function is used here

def merge_sort(X):
    print('X : ', X)
    if len(X) > 1:
        mid = len(X)//2
        left_half  = X[:mid]
        right_half = X[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        while(i < len(left_half)) and (j < len(right_half)):
                            if left_half[i] < right_half[j]:
                                X[k] = left_half[i]
                                i += 1
                            else:           
                                X[k] = right_half[j]
                                j += 1
                            k += 1
        while(i < len(left_half)):
              X[k] = left_half[i]
              i += 1
              k += 1
        while(j < len(right_half)):
              X[k] = right_half[j]
              j += 1
              k += 1
    print('merged list: ', X)

merge_sort(X)
