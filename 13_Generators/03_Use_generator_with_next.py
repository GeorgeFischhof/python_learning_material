
def get_square_numbers():
    number = 1
    while True:
        yield number ** 2
        number += 1


squares = get_square_numbers()  # squares is a generator object
print(next(squares))  # the generator object can be called with "next"
print(next(squares))
print(next(squares))
print()
print('3 numbers will be enough now')
