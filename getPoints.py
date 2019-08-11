def getPoints(answers, p):
    questionPoints = lambda x,y : x+1 if y else p*-1

    res = 0
    for i, ans in enumerate(answers):
	print(questionPoints(i, ans))
        res += questionPoints(i, ans)
    return res

