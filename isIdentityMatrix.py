isIdentityMatrix = lambda a : all([a[i][j]==1 and i ==j or a[i][j] == 0 and i!=j for i in range(len(a)) for j in range(len(a)) ] )
