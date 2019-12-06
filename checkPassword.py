def checkPassword(attempts, password):
    def check():
        while True:
            yield True if attempt == password else False

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1

print(checkPassword(["hello",  "world",  "I",  "like",  "coding"], "like"))
