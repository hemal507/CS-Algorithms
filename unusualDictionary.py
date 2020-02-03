def unusualDictionary(wordList):
    return wordList == sorted(wordList, key=lambda k: (k.split()[-1], k))
