

# Map function executes a function (first parameter) on all elements of an iterable (second parameter)
# map(function_to_execute, iterable_contains_parameters_for_function)

# convert a series of 1 and 0 to binary and then to decimal representation

numbers = [1, 0, 1, 0]

numbers_text = ''.join(list(map(str, numbers)))
print('Binary string: ', numbers_text)

decimal_from_binary = int(numbers_text, 2)
print('decimal: ', decimal_from_binary)

print()

# ---

# print list items one in each line

fruits_list = ['list', 'apple', 'banana', 'lemon']
list(map(print, fruits_list))

print()

fruits_for = ['for', 'apple', 'banana', 'lemon']
for tmp in map(print, fruits_for):
    pass
