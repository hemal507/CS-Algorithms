def mathPractice(numbers):
    return reduce(lambda acc, (x,y): acc + y if x%2 else acc * y, enumerate(numbers), 1)

