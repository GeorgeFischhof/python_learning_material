
# https://docs.python.org/3/library/collections.html#collections.namedtuple

# Data structure that behaves like a database record
# indexable, iterable, and fields can be accessed by their name
# with this we can create more readable, self-documenting code

'''

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

typename: the name showed in __repr__()
field_names: list of strings containg the field names
typename and field name syntax is same as variable names

'''

from collections import namedtuple

Person = namedtuple(
    'Basic_person_data',
    ['first_name', 'last_name', 'age', 'gender']
)

person_1 = Person('Jane', 'Doe', 42, 'female')
person_2 = Person(
    first_name='John',
    last_name='Doe',
    gender='male',
    age=24,
)

print(person_1)
# Basic_person_data(first_name='Jane', last_name='Doe', age=42, gender='female')

print(person_2.first_name, person_2.last_name)
# John Doe
