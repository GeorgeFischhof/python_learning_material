
# https://docs.python.org/3/library/collections.html#collections.Counter

# counts elements in a list and returns a dict where
# keys are elements of the list
# values are the number of occurrences for each element

'''

collections.Counter([iterable-or-mapping])

methods
-------

elements()
Return an iterator over elements repeating each
as many times as its count.
Elements are returned in arbitrary order.
If an element’s count is less than one, elements() will ignore it

most_common([n])
Return a list of the n most common elements
and their counts from the most common to the least.
If n is omitted or None, most_common() returns all elements in the counter.
Elements with equal counts are ordered arbitrarily

subtract([iterable-or-mapping])
Elements of the parameter are subtracted from original

'''

from collections import Counter

colors = [
    'red',
    'red', 'blue',
    'red', 'blue', 'green',
    'red', 'blue', 'green', 'white',
    'red', 'blue', 'green', 'white', 'black',
]

number_of_colors = Counter(colors)

print(number_of_colors)
# Counter({'red': 5, 'blue': 4, 'green': 3, 'white': 2, 'black': 1})

print(number_of_colors.most_common(3))
# [('red', 5), ('blue', 4), ('green', 3)]

decrease_colors = ['red', 'red']
number_of_colors.subtract(decrease_colors)
print(number_of_colors)
# Counter({'blue': 4, 'red': 3, 'green': 3, 'white': 2, 'black': 1})
