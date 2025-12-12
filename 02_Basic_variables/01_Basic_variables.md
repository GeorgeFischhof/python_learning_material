

# Basic variables


**Keywords**

https://docs.python.org/3/reference/lexical_analysis.html#keywords

**Built-in Functions**

https://docs.python.org/3.14/library/functions.html

DO NOT CREATE ANYTHING WITH THE NAMES FOUND ON ABOVE LINKS ;-) <br/>
Anything other is good. <br/>
==> overwrite_builtins.py


## Basic variable types

Python supports different type of variables such as
- integer (int) - whole numbers
- floating point (float) - numbers with fractions
- string (str) - holds text (characters, not bytes)
- bool (bool) - represents the truth, value can be True or False <br/>

- NoneType - the value None represents the absence of a value,
  it is not equal to empty value. Type of None is NoneType <br/>

- decimal.Decimal - working with non integer decimal numbers very big precision
- fractions.Fraction - operates with fraction numbers (3/4)
- complex (complex) - for complex numbers <br/>

- bytes, bytearray, memoryview - for manipulating binary data


You do not need to specify the type of the variables,
you can simply assign any value to a variable,
Python will take care about its type

Text must be enclosed into string delimiters which can be:
apostrophe `'`
or
double quote `"` (this is the preferred one)
The string can contain the other delimiter


Assignment is created with equal sign `=`


### Examples

- `some_integer = 42         # int (integer) a whole number`
- `some_float = 3.1415926    # float a number with decimal digits`  <br/> <br/>

- `name = 'Python'           # a string`
- `name = "Python"           # a string`
- `it_is_good = "It's good"  # The string can contain the other delimiter` <br/> <br/>

- `apple_is_fruit = True     # Bool true`
- `apple_is_animal = False   # Bool false`


To modify the value of a variable
to a value which is relative to current value,
you can use the current value on the right side:

For example we can increase the value of a numeric variable:
```python
some_value = 10
some_value = some_value + 2
```

shortened version for increasing:
```python
some_value = 10
some_value += 2
```

## Variable names

Identifiers (names of variables, functions, classes, modules)

- can contain
  - lower case letters: a to z
  - upper case letters: A to Z
  - digits: 0 to 9
  - underscore: _
- can not start with a digit
- keywords can not be used

