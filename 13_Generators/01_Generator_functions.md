# Generators - Generator functions

<https://realpython.com/introduction-to-python-generators/>

Memory efficient list-like stuff.<br/>
Can be very useful when you have large amount of data,
and you can process it by chunks or item-by-item.<br/>
For example large number of large files. ...

Generates one element at a time.

The usage can be started after the first element is generated.

We can use `for` cycle to iterate over it, like it was a list.

# Syntax

## yield

The `yield` statement is used in a function to return a value.

The state of the function is saved, and the next
function "call" will continue the execution of the function.

```python
def infinite_sequence():
    number = 0
    while True:
        yield number
        number += 1
```

# Usage

## for cycle

Just as it would be a list:

```python
for number in infinite_sequence():
    print(number)
# 0, 1, 2 ...
```

## next

Instead of using the for cycle we can simulate it with the  
`next` function for the iteration — until the generator is exhausted.

## exhausted

When the generator is exhausted it will raise<br/>
`StopIteration` exception (the `for` cycle uses this to
finish the cycle).
