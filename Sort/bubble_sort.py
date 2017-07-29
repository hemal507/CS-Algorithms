import numpy as np


# generate a random array
#X = np.random.randint(1000,size=10)
##X=[242, 903 , 751 ,219 ,775 ,102, 314 ,687 ,320 ,300 ,859]
X = [7,8,5,4,9,2]
##X = [2,1,4,5,7,8,9]
print('UNSORT: ', X)

## compare adjacent elements
## at the end of each outer loop iteration, one element towards right get sorted

for i in range(0, len(X)-1):
    print('Main loop : ' ,i , 'X :      ' , X)
    for j in range(0, len(X)-1-i, 1):
            if X[j] > X[j+1]:
                X[j], X[j+1] = X[j+1], X[j]
                print('    Inner loop: ' , j , " X : " , X)
            else:
                print('    Inner NOSR: ' , j , " X : " , X)
print("SORTED: ", X)
        

