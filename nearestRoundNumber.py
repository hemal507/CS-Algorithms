def nearestRoundNumber(n) :
	return n+(10-(n%10)) if (n%10) != 0 else n

print(nearestRoundNumber(130))
