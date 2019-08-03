'''
Given integers a and b, determine whether the following pseudocode results in an infinite loop
while a is not equal to b do
  increase a by 1
  decrease b by 1
'''

def isInfiniteProcess(a,b) :
	d = abs((a-b)/2)
	if a+d == b-d :
		return False
	return True		


print(isInfiniteProcess(2,6))
print(isInfiniteProcess(2,10))
print(isInfiniteProcess(10,10))
print(isInfiniteProcess(6,10))
print(isInfiniteProcess(2,3))
print(isInfiniteProcess(0,1))
print(isInfiniteProcess(3,1))
print(isInfiniteProcess(5,10))
print(isInfiniteProcess(10,0))
