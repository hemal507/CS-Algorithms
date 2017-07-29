import numpy as np


# generate a random array
#X = np.random.randint(1000,size=10)
##X=[242, 903 , 751 ,219 ,775 ,102, 314 ,687 ,320 ,300 ,859]
X = [7,8,1,5,4,9,2]
##X = [2,1,4,5,7,8,9]
print('UNSORT:       ', X)

## selection sort

## It finds the smallest among the list and swaps with first element
## It moves to 2nd and starts searching for smallest in unsorted list
## swaps with 2nd and so on...

for i in range(0,len(X)-1):
    min_index = i
##    min_value = X[i]
    for j in range(i+1,len(X)):
                    if X[j] < X[min_index]:
                        min_index = j
    if min_index != i:                        
        X[i], X[min_index] = X[min_index], X[i]
        print('Swapped list: ', X)

print('Sorted list:  ' , X)    
            
            
