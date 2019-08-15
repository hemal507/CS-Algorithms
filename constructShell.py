def constructShell(n) :
	return  [[0]*i for i in range(1,n+1) ]  +  [[0]*j for j in range(n-1,0,-1)  ]

print(constructShell(5))
