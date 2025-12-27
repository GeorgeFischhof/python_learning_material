# Important built-in functions

<https://docs.python.org/3/library/functions.html>

## print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

Print objects to the text stream file, separated by `sep` and followed by `end`. <br/>  
`sep`, `end`, `file` and `flush`, if present, must be given as keyword arguments.

String interpolation:  
<https://docs.python.org/3/library/string.html#formatspec>  
<https://pyformat.info/>  
<https://realpython.com/python-f-strings/>

## input([prompt])

If the prompt argument is present, it is written to standard output without a trailing newline. <br/>  
The function then reads a line from input, converts it to a string (stripping a trailing newline),  
and returns that. <br/>  
If the `readline` module was loaded, then `input()` will use it to provide line editing and history features.

## all(iterable)

Return `True` if all elements of the iterable are true (or if the iterable is empty).

## any(iterable)

Return `True` if any element of the iterable is true. <br/>
If the iterable is empty, return `False`.

## chr(i)

Return the string representing a character whose Unicode code point is the integer `i`. <br/>  
This is the inverse of `ord()`.

## class - dict(**kwarg) | dict(mapping, **kwarg) | dict(iterable, **kwarg)

Create a new dictionary.

## dir([object])

Without arguments, return the list of names in the current local scope. <br/>  
With an argument, attempt to return a list of valid attributes for that object.

## divmod(a, b)

Take two (non-complex) numbers as arguments and return a pair consisting of their quotient and remainder.

## enumerate(iterable, start=0)

Return a tuple containing a count (from `start`, which defaults to 0) and 
the values obtained from iterating over `iterable`

## eval(expression, globals=None, locals=None)

The arguments are a string and optional `globals` and `locals`. <br/>
If provided, `globals` must be a dictionary. If provided, `locals` can be any mapping object.  
The expression argument is parsed and evaluated as a Python expression.

## exec(object[, globals[, locals]])

Supports dynamic execution of Python code.  
`object` must be either a string or a code object.  
If it is a string, it is parsed as a suite of Python statements and executed.  
(Can be dangerous if `object` is unchecked user input.)

## filter(function, iterable)

Construct an iterator from those elements of `iterable` for which `function` returns true.

## class - float([x])

Return a floating point number constructed from a number or string `x`.

## format(value[, format_spec])

Convert a value to a “formatted” representation, as controlled by `format_spec`. <br/>  
Formatting syntax:  
<https://docs.python.org/3/library/string.html#formatspec>  
<https://pyformat.info/>  
<https://realpython.com/python-f-strings/>

## getattr(object, name[, default])

Return the value of the named attribute of `object`. <br/>
If the attribute does not exist, return `default` if provided, otherwise raise `AttributeError`.

## globals()

Return a dictionary representing the current global symbol table.<br/>
This is always the dictionary of the current module (inside a function or method, this is
the module where it is defined, not the module from which it is called)

## hasattr(object, name)

Return `True` if the string is the name of one of the object’s attributes, `False` otherwise.

## hex(x)

Convert an integer number to a lowercase hexadecimal string prefixed with `"0x"`.

## class - int([x]) | int(x, base=10)

Return an integer object constructed from a number or string `x`, or return 0 if no arguments are given.

## isinstance(object, classinfo)

Return `True` if `object` is an instance of `classinfo` or its subclass.

## issubclass(class, classinfo)

Return `True` if `class` is a subclass (direct, indirect or virtual) of `classinfo`.

## len(s)

Return the length (number of items) of an object.

## class - list([iterable])

`list` is a mutable sequence type. <br/>
Returns a list object.

## locals()

Update and return a dictionary representing the current local symbol table.

## map(function, iterable, ...)

Return an iterator that applies `function` to every item of `iterable`, yielding results. <br/>  
If multiple iterables are passed, `function` must accept that many arguments. <br/>  
Stops when the shortest iterable is exhausted.<br/>
For cases where the function inputs are already
arranged into argument tuples, see itertools.starmap().

## max(iterable, *[, key, default]) | max(arg1, arg2, *args[, key])

Return the largest item in an iterable or the largest of two or more arguments.

## min(iterable, *[, key, default]) | min(arg1, arg2, *args[, key])

Return the smallest item in an iterable or the smallest of two or more arguments.

## next(iterator[, default])

Retrieve the next item from the iterator by calling its `__next__()` method.  
If `default` is given, it is returned if the iterator is exhausted; otherwise `StopIteration` is raised.

## oct(x)

Convert an integer number to an octal string prefixed with `"0o"`.

## open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Open a file and return a corresponding file object.  
If the file cannot be opened, an `OSError` is raised.

## ord(c)

Given a string representing one Unicode character, return its Unicode code point.  
For example, `ord("a")` returns 97 and `ord("€")` returns 8364. <br/>
This is the inverse of `chr()`.

## pow(x, y[, z])

Return `x` to the power `y`. <br/>
If `z` is present, return `x` to the power `y`, modulo `z`.

## range(stop) | range(start, stop[, step])

`range` is an immutable sequence type. <br/>
Returns integers from start to stop with steps.

## repr(object)

Return a string containing a printable representation of an object. <br/>
Mainly used for debugging. <br/>
See `str()`. <br/>

## reversed(seq)

Return a reverse iterator.

## round(number[, ndigits])

Return `number` rounded to `ndigits` precision after the decimal point. <br/>
If `ndigits` is omitted or `None`, return the nearest integer.

## class - set([iterable])

Return a new set object, optionally with elements taken from `iterable`.

## setattr(object, name, value)

Assign a value to an attribute of an object.  
Equivalent to `object.name = value`.

## sorted(iterable, *, key=None, reverse=False)

Return a new sorted list from the items in `iterable`. <br/>
Sorting HOWTO:  
<https://docs.python.org/3/howto/sorting.html#sortinghowto>

## class - str(object="") | str(object=b"", encoding="utf-8", errors="strict")

Return a string version of `object`. <br/>
`print()` uses `str()` to write out objects.

## sum(iterable[, start])

Sums `start` and the items of an iterable from left to right. <br/>
`start` defaults to 0. <br/>
Items are normally numbers; `start` cannot be a string.

Alternatives:  
- `"".join(sequence)` for fast string concatenation  
- `math.fsum()` for precise floating point addition  
- `itertools.chain()` for concatenating iterables

## super([type[, object-or-type]])

Return a proxy object that delegates method calls to a parent or sibling class of `type`.
This is useful for accessing
inherited methods that have been overridden in a class.
The search order is same as that used by getattr()
except that the type itself is skipped.

## tuple([iterable])

`tuple` is an immutable sequence type.<br/>
Returns a tuple object.

## class - type(object) | type(name, bases, dict)

With one argument, return the type of an object.  

The isinstance() built-in function is recommended
for testing the type of an object, because it
takes subclasses into account.

With three arguments, create a new type object dynamically. <br/>
(Not used, just for the completeness)<br/>
This is essentially a dynamic form of the class
statement. The name string is the class name and
becomes the __name__ attribute; the bases tuple
itemizes the base classes and becomes the __bases__
attribute; and the dict dictionary is the namespace
containing definitions for class body and is copied
to a standard dictionary to become the __dict__
attribute.

## vars([object])

Return the `__dict__` attribute for a module, class, instance, or any object with a `__dict__`.  
Without an argument, `vars()` acts like `locals()`.

## zip(*iterables)

Make an iterator that aggregates elements
from each of the `iterables`.

Returns an `iterator` of `tuples`, where the i-th tuple contains
the i-th element from each of the argument sequences or
iterables. The iterator stops when the shortest input
iterable is exhausted. With a single iterable argument,
it returns an iterator of 1-tuples.
