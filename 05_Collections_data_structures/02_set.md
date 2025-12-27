# Set, frozenset

Sets are sets :-) as we learned them from mathematics.<br/>
Sets can have any types of item,<br/>
the types can be different as well (like in the lists).

Sets are unordered, and item duplication is not allowed.

To define a set use braces `{}` or the `set()` or `frozenset()` constructor.

Set is mutable, frozenset is immutable.

## example

```python
even_numbers = {2, 4, 6,}
# the last comma is not a typo, it is allowed,
# in fact sometimes it is very good

odd_numbers = set((1, 3, 5))
prime_numbers = set([2, 3, 5, 7])
# The set constructor constructs the set from a list or tuple
```

Empty set can be defined with the following instruction:<br/>
`empty_set = set()`

Using the formula:<br/>
`something = {}`<br/>
will create an empty dictionary.

# Set operators

## union

```python
a + b
a | b
a.union(b)
```

## intersection

```python
a & b
a.intersection(b)
```

## difference

```python
a - b
a.difference(b)
```

## symmetric difference

```python
a ^ b
a.symmetric_difference(b)
```

# Set comparison

## isdisjoint(other)

Return `True` if the set has no elements in common with `other`.<br/>
Sets are disjoint if and only if their intersection is the empty set.

## issubset(other)  
`set <= other`

Test whether every element in the set is in `other`.

## `set < other`

Test whether the set is a proper subset of `other`,<br/>
that is, `set <= other` and `set != other`.

## issuperset(other)  
`set >= other`

Test whether every element in `other` is in the set.

## `set > other`

Test whether the set is a proper superset of `other`,<br/>
that is, `set >= other` and `set != other`.

# To check if an element is in or not in the set

```python
if 3 in odd_numbers:
    print("3 is odd")

if 2 not in odd_numbers:
    print("2 is even")
```

# Get all items of a set

```python
for item in odd_numbers:
    print(item)
```

Some graphic and code:  
<https://www.programiz.com/python-programming/set>
