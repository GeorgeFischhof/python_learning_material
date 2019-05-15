
def exhaust_squares():
    yield 1
    yield 4


squares = exhaust_squares()
print()
print(squares)
print()
print(next(squares))
print(next(squares))
print(next(squares))
