
import sys

even_numbers_generator = (number for number in range(51) if number % 2 == 0)
print(next(even_numbers_generator))  # ==> 0
print(next(even_numbers_generator))  # ==> 2
print(next(even_numbers_generator))  # ==> 4
print()

# for cycle uses "next" under the hood

for even_number in even_numbers_generator:
    print(even_number, end=' ')  # ==> 6 8 10 12 ...


print()
even_numbers_list = [number for number in range(51) if number % 2 == 0]
print('Size of generator:', sys.getsizeof(even_numbers_generator))
print('Size of list:', sys.getsizeof(even_numbers_list))



