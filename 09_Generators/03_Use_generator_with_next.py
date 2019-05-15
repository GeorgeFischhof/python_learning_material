
def get_square_numbers():
    number = 1
    while True:
        yield number ** 2
        number += 1


squares = get_square_numbers()
print(next(squares))
print(next(squares))
print(next(squares))
print()
print('3 numbers will be enough now')
