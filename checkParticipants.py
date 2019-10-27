def checkParticipants(participants):
    return [x for x,y in enumerate(participants) if y < x]
