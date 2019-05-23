
# Unpacking
# =========

# Operators
# ---------

# list unpacking: *
# dict unpacking: **


def function_with_unknown_number_of_parameters(known, default=None, *args, **kwargs):
    print('known  = ', known)     # ==> 1
    print('default = ', default)  # ==> 2
    print('* * *')

    print('args = ', args)        # ==> (3, 4) tuple
    print('kwargs = ', kwargs)    # ==> {'a': 5, 'b': 6, 'c': 7} dict


function_with_unknown_number_of_parameters(1, 2, 3, 4, a=5, b=6, c=7)


print('\n* * * * * *\n')


my_list = [1, 2, 3, 4, 5]


print('*beginning, last_item = my_list')
*beginning, last_item = my_list

print('*beginning = ', beginning)   # ==> [1, 2, 3, 4]
print('last_item = ', last_item)    # ==> 5


print('\n* * * * * *\n')


print('first_item, *middle, last_item = my_list')
first_item, *middle, last_item = my_list

print('first_item = ', first_item)  # ==> 1
print('*middle = ', middle)         # ==> [2, 3, 4]
print('last_item = ', last_item)    # ==> 5


print('\n* * * * * *\n')


print('first, *ending = my_list')
first, *ending = my_list

print('first = ', first)            # ==> 1
print('*ending = ', ending)         # ==> [2, 3, 4, 5]


print('\n* * * * * *\n')

# merging dicts

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
# z = {**x, **y}                    # ONLY from Python version 3.5

# print(z)                          # ==> {'a': 1, 'b': 3, 'c': 4}
