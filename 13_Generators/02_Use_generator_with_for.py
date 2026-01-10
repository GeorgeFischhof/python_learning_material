
def get_even_numbers():
    print()
    print("The function state is saved at yield")
    print("These texts are printed only once")

    number = 0
    while number < 11:
        yield number
        number += 2


for even_number in get_even_numbers():
    print(even_number)
