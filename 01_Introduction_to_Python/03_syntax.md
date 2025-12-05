

# Syntax

A program consists of the following building blocks:

- sequence (of steps)
- conditional (steps)
- loop (ing steps)

Instructions that initiate a group of other instructions (called a block) — for example conditions,
loops, function definitions, with statements and classes — are terminated with a colon `:` and the
block must be indented with 4 spaces.

Examples:

```python
if a == 1:
    pass

for i in range(3):
    pass

def some_function():
    pass
```

## Comments


Comments are started with hash mark `#`. Anything after `#` on the same line is ignored by Python.

Examples:

```python
# This is a commented line, this will not be executed
print('apple') # Comment starts here, apple will be printed, nothing else happens
```


## Python is Case sensitive


The keywords are all in lower case.
variables, modules, packages, classes, constants can contain upper case letters, but
case sensitivity remains:
`variable1` not equals to `Variable1`

```python
>>> variable1 = 42
>>> Variable1 = 'apple'
>>> print(variable1)
42
>>> print(Variable1)
apple
```

According to [PEP-8](https://www.python.org/dev/peps/pep-0008/), which is the Python coding style accepted by the community and used by millions the
- variables, functions written in snake case: lower case letters with underscore `_` between the words
- classes are written in Pascal Camal case, ot giraffe case: every (even the first) word starts with uppercase
- constants (which would mean really constants) are written in all upper case letters


## Indentation matters

Indentation determines block structure. Misplaced indentation changes program flow or raises errors. The following shows how indentation affects output.

Example with block indentation:

```Python
>>> for i in range(3):
...     print(i)
...     print('finished')
0
finished
1
finished
2
finished
```

Example without intended block:

```Python
>>> for i in range(3):
>>>     print(i)
>>> print('finished')
0
1
2
finished
```


## One command per line

There is a possibility to write more instructions in one line,
the separator is semicolon ;

But it is not readable, do not do this (should be reserved for rare cases)

And actually there are only some very rare cases,
when there is a need to write more instructions into one line
