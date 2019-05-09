
# Returning multiple values
# It is possible to return more values in a function
#
# Python implicitly packs the values into a tuple


def function_returns_multiple_values():
    return 5, 'apple'


# one way to use the values, when you
# assign the returned values to variables one-by-one

number_of_fruits, type_of_fruits = function_returns_multiple_values()
print()
print('number_of_fruits: ', number_of_fruits)
print('type_of_fruits: ', type_of_fruits)
print()


# the other way is to use them as a tuple

packed_fruits = function_returns_multiple_values()
print('packed_fruits: ', packed_fruits)
print('elements of tuple: [0] =', packed_fruits[0], ' [1] =', packed_fruits[1])
print('type of packed_fruits: ', type(packed_fruits))


'''
Tips on returning multiple values
---------------------------------

1.) Grouping  
You can create a group by wrap your stuff into parenthesis
And because it is grouped it can reside multiple lines  

def function_returns_multiple_values():
    return (
        5,
        'apple',
    )

Note grouping is a general technique for multi-line stuff,
actually in this case you explicitly create a tuple   


2.) Consider using dict
When you return multiple values, 
the upper layers of your program 
(the functions that call the one which returns multiple values) 
must take care with the returned values.

If the values are in a tuple, 
you have to access them by index or by order
 
packed_fruits[0], packed_fruits[1]
number_of_fruits, type_of_fruits = function_returns_multiple_values()

You are not able to insert a value between the existing ones
without rewriting the upper layers.

If you use a dict, the returned values can be accessed by a key,
which identifies the returned value.
If there is a need, you can add any number of new values without 
any change in the existing caller functions  

'''

input('Return with dict')
print('\n* * * * * * * * * *\n')


def get_some_fruits():
    fruits = {
        'number_of_fruits': 5,
        'color_of_fruits': 'red',
        'type_of_fruits': 'apple',
    }
    return fruits


print('Existing fruit eaters - callers')
today_fruits = get_some_fruits()
print('We have {number} pieces of {fruit} to eat today'
      .format(number=today_fruits['number_of_fruits'],
              fruit=today_fruits['type_of_fruits']))

print()
print('New requirement: I do not like yellow apples')
print('What color of fruits we got?')
print('We have {color} fruits now.'
      .format(color=today_fruits['color_of_fruits']))
