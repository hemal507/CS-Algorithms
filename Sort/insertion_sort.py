import numpy as np


# generate a random array
#X = np.random.randint(1000,size=10)
##X=[242, 903 , 751 ,219 ,775 ,102, 314 ,687 ,320 ,300 ,859]
X = [7,8,1,5,4,9,2]
##X = [2,1,4,5,7,8,9]
print('UNSORT: ', X)

## insertion sort
## start with second element;
## compare it with previous all elements in list 
## if they are NOT in order, swap until it is placed in order

for i in range(1, len(X)):
    print('Main loop : ' ,i , 'X :      ' , X, ' Comparing: ' ,X[i])
    for j in range(i-1, -1, -1):
            if X[j] > X[j+1]:
                X[j], X[j+1] = X[j+1], X[j]
                print('    Inner loop: ' , j , " X : " , X)
            else:
                print('    Inner NOSR: ' , j , " X : " , X)
                break
    print("\n")       
print("SORTED: ", X)
        

# optimized - shifts instead of swapping		
##for i in range(1, len(X)):
##    curNum = X[i]
##    k=0
##    print('Main loop : ' ,i , 'X :      ' , X , 'curNum  ', curNum )
##    for j in range(i-1, -2, -1):
##                                        k=j
##                                        if X[j] > curNum:
##                                            
##                                            X[j+1] = X[j]
##                                            print('    Inner loop: ' , j , " X : " , X)
##                                        else:
##                                            
##                                            break
##    X[k+1] = curNum
##    print('Outr loop : ' ,i , 'X :      ' , X , 'curNum  ', curNum )
##print("SORTED: ", X)
##		


