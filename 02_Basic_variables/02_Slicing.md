
# Slicing

- Get one part of a string by index
- Possibility to get characters with given steps
- Sometimes called extended indexing

It works with lists too.


## syntax
------
str[start:stop:step]

All parameters are optional

start defaults to 0        (start index starts with 0)
stop  defaults to len(str) (stop index starts with 1)
step  defaults to 1

all parameters can be negative, it means execute from right,
the last character is -1


One way to remember how slices work is to think of the
indices as pointing between characters, with the left
edge of the first character numbered 0. Then the right
edge of the last character of a string of n characters
has index n, for example:

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1


Examples
--------

'0123456789'[2]      # == > '2'

'0123456789'[:4]     # == > '0123'

'0123456789'[4:]     # == > '456789'

'0123456789'[0:2]    # == > '01'

'0123456789'[2:4]    # == > '23'

'0123456789'[-3]     # == > '7'

'0123456789'[-3:]    # == > '789'

'0123456789'[::2]    # == > '02468'

'0123456789'[2:8:2]  # == > '246'

'0123456789'[::-1]   # == > '9876543210'


Note: you can create a slice object if you want to
slice with the same parameters several times, or
if you want to give a name to the slicing numbers.
https://docs.python.org/3/library/functions.html#slice

get_every_second_from_middle = slice(1, -2, 2)
print('0123456789'[get_every_second_from_middle])  # ==> '1357'

get_every_second = slice(None, None, 2)
print('0123456789'[get_every_second_from_middle])  # ==> '02468'
