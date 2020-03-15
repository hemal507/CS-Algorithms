def companyBotStrategy(trainingData):
    if len([x[0] for x in trainingData if x[1] == 1 ]) == 0 :
            return 0.0
    return (sum([x[0] for x in trainingData if x[1] == 1 ]) / (sum([x[1] for x in trainingData if x[1] == 1 ]) * 1.0 ) )

